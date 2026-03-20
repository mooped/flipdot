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

def mulmv(a, b):
  return nary(lambda a, b: sum(mul(a, b)), a, (b, b, b))

#def mulmm(a, b):

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

transform = [ [  1.0000000,  0.0000000,  0.0000000  ],
              [  0.0000000,  0.8191521, -0.5735765  ],
              [  0.0000000,  0.5735765,  0.8191521  ], ]

def orbit(period, distance, t):
  ang = t * 2.0 * math.pi
  return mulmv(transform, muls((math.cos(ang / period), 0.0, math.sin(ang / period)), distance))

def orreray(ray, t, pos):
  planets = [
    (pos, 695700.0 / 40.0),
    (add(pos, orbit(88, 57900000, t)), 2440.0),
    (add(pos, orbit(255.0, 108200000, t)), 6052.0),
    (add(pos, orbit(365.0, 149600000, t)), 6371.0),
    (add(pos, orbit(687.0, 227900000, t)), 3390.0),
    (add(pos, orbit(4333.0, 778600000, t)), 69911.0),
    (add(pos, orbit(10759.0, 1433500000, t)), 58232.0),
    (add(pos, orbit(30687.0, 2872500000, t)), 25362.0),
    (add(pos, orbit(60190.0, 4495100000, t)), 24622.0),
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

def raycast(x, y, t):
  ray = rays[y][x]
  return orreray(ray, t, (0.0, 0.0, 238000000.0))

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

