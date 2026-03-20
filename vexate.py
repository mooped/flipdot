import argparse
import base64
import math
import operator
import paho.mqtt.client as mqtt
import random
import subprocess
import time

import decode

parser = argparse.ArgumentParser(prog="Hexate",description="Flipdot Distance Field Renderer")
parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()

def nary(op, *args):
  return tuple(map(lambda x: op(*x), zip(*args)))

def add(a, b):
  return nary(operator.add, a, b)

def sub(a, b):
  return nary(operator.sub, a, b)

def mul(a, b):
  return nary(operator.mul, a, b)

def muls(a, b):
  return nary(lambda x: x * b, a)

def divs(a, b):
  return nary(lambda x: x / b, a)

def dot(a, b):
  return sum(mul(a, b))

def lengthsq(a):
  return dot(a, a)

def length(a):
  return math.sqrt(dot(a, a))

def normalize(a):
  return divs(a, length(a))

def mix(x, y, a):
  return x * (1.0 - a) + y * a

def smin(a, b, k):
  h = max(0.0, min(1.0, 0.5 + 0.5 * (b - a) / k))
  return mix(b, a, h) - k * h * (1.0 - h)

def sphere(x, y, z, pos, rad):
  return length(sub(pos, (x, y, z))) - rad

def orbit2(x, y, z, t, pos):
  k = 3.0
  dist = 4.0 * (20.0 + t)
  ang = 9.0 * t / (2.0 * math.pi)
  return smin(
    sphere(x, y, z, add(pos, muls((math.cos(ang), math.sin(ang), 0.0), dist)), 10),
    sphere(x, y, z, sub(pos, muls((math.cos(ang), math.sin(ang), 0.0), dist)), 20),
    k)

def orrerey(x, y, z, t, pos):
  ang = 100000.0 + 900.0 * t
  return min(
    sphere(x, y, z, pos, 1391400.0),
    sphere(x, y, z, add(pos, muls((math.cos(ang / 88.0), 0.0, math.sin(ang / 88.0)), 57900000)), 4879.0),
    sphere(x, y, z, add(pos, muls((math.cos(ang / 225.0), 0.0, math.sin(ang / 225.0)), 108200000)), 12104.0),
    sphere(x, y, z, add(pos, muls((math.cos(ang / 365.0), 0.0, math.sin(ang / 365.0)), 149600000)), 12756.0),
    sphere(x, y, z, add(pos, muls((math.cos(ang / 687.0), 0.0, math.sin(ang / 687.0)), 227900000)), 6792.0),
    sphere(x, y, z, add(pos, muls((math.cos(ang / 4333.0), 0.0, math.sin(ang / 4333.0)), 778600000)), 142984.0),
    sphere(x, y, z, add(pos, muls((math.cos(ang / 10759.0), 0.0, math.sin(ang / 10759.0)), 1433500000)), 120536.0),
    sphere(x, y, z, add(pos, muls((math.cos(ang / 30687.0), 0.0, math.sin(ang / 30687.0)), 2872500000)), 51118.0),
    sphere(x, y, z, add(pos, muls((math.cos(ang / 60190.0), 0.0, math.sin(ang / 60190.0)), 4495100000)), 49528.0),
  )

def dist(x, y, z, t):
  #d = sphere(x, y, z, (0, 0, 40), 15.0)   # Sphere in the centre of the display
  #d = orbit2(x, y, z, t, (0.0, 0.0, 40.0))
  d = orrerey(x, y, z, t, (0.0, 0.0, 2380000000.0))
  return d#0 if math.modf(d * 0.1)[0] <= 0.5 else 1

# Distance along ray until intersection with a sphere
def raysphere(ray, pos, radius):
  # Project ray onto pos, assume ray is already normalised
  proj = dot(ray, pos)
  # Nearest point on the ray to the centre of the sphere
  nearest = muls(ray, proj)
  # Distance squared from ray to centre of sphere
  distsq = lengthsq(sub(nearest, pos))
  # Did we hit?
  if distsq < (radius * radius):
    # Intersection point forms a triangle with the projected point and the sphere centre
    intersection = sub(nearest, muls(ray, math.sqrt(radius * radius + distsq)))
    return math.sqrt(distsq), intersection
  return None

def orreray(ray, t, pos):
  ang = t * 2.0 * math.pi
  planets = [
    (pos, 695700.0 / 40.0),
    (add(pos, muls((math.cos(ang / 88.0), math.sin(ang / 88.0), 0.0), 57900000)), 2440.0),
    (add(pos, muls((math.cos(ang / 225.0), math.sin(ang / 225.0), 0.0), 108200000)), 6052.0),
    (add(pos, muls((math.cos(ang / 365.0), math.sin(ang / 365.0), 0.0), 149600000)), 6371.0),
    (add(pos, muls((math.cos(ang / 687.0), math.sin(ang / 687.0), 0.0), 227900000)), 3390.0),
    (add(pos, muls((math.cos(ang / 4333.0), math.sin(ang / 4333.0), 0.0), 778600000)), 69911.0),
    (add(pos, muls((math.cos(ang / 10759.0), math.sin(ang / 10759.0), 0.0), 1433500000)), 58232.0),
    (add(pos, muls((math.cos(ang / 30687.0), math.sin(ang / 30687.0), 0.0), 2872500000)), 25362.0),
    (add(pos, muls((math.cos(ang / 60190.0), math.sin(ang / 60190.0), 0.0), 4495100000)), 24622.0),
  ]
  nearest = None
  for (p, r) in planets:
    hit = raysphere(ray, p, r * 2000.0)
    if hit:
      return 1
  return 0

# Precompute ray directions (because why not)
# Put the centre of the screen 20 units from the camera down z
rays = []
for y in range(8):
  row = []
  for x in range(84):
    row.append(normalize((x - 41.5, y - 3.5, 20.0)))
  rays.append(row)

def raycastdf(x, y, t):
  ray = rays[y][x]
                                # Start tracing at the screen to ignore anything behind it
  c = add(muls(ray, 20.0), (0.0, 0.0, 5.0 * t))
  d = 0.0
  for step in range(50):        # Trace 25 steps before giving up
    d = dist(c[0], c[1], c[2], t)
    c = add(c, muls(ray, d))    # March along the ray by the last distance
    if d < 100000000.0:         # Hit (close enough)
      return 1
  return 0                      # Miss

def raycast(x, y, t):
  ray = rays[y][x]
  return orreray(ray, t, (0.0, 0.0, 238000000.0))#2380000000.0))

def encode(grid):
  buffer = []
  g = zip(*grid)
  for col in g:
    value = 0
    bv = 1
    for bit in col:
      value += bit * bv
      bv = bv << 1
    buffer.append(value)
  return bytearray(buffer)

def frame(t):
  grid = []
  
  for y in range(8):
    row = []
    for x in range(84):
      row.append(raycast(x, y, t))
    grid.append(row)
  
  return encode(grid)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect('localhost')
mqttc.loop_start()

def set_buffer(index):
  mqttc.publish('nh/flipdot/comfy/buffer', index)

def send_raw(message):
  mqttc.publish('nh/flipdot/comfy/raw', message)

def send_text(message):
  mqttc.publish('nh/flipdot/comfy/text', message)

#set_buffer(6)

for t in range(365):
  f = frame(t)
  #send_raw(f)
  if args.verbose:
    decode.output(f)
  #time.sleep(0.5)

#send_text("CONTAINMENT!")

#time.sleep(10)
#set_buffer(0)

mqttc.loop_stop()

