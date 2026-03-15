import base64
import math
import random
import sys
import time

import decode

def add(a, b):
  (xa, ya) = a
  (xb, yb) = b
  return (xa + xb, ya + yb)

def sub(a, b):
  (xa, ya) = a
  (xb, yb) = b
  return (xa - xb, ya - yb)

def mul(a, b):
  (xa, ya) = a
  (xb, yb) = b
  return (xa * xb, ya * yb)

def muls(a, b):
  (xa, ya) = a
  return (xa * b, ya * b)

def length(a):
  x, y = a
  return math.sqrt(x * x + y * y)

def mix(x, y, a):
  return x * (1.0 - a) + y * a

def smin(a, b, k):
  h = max(0.0, min(1.0, 0.5 + 0.5 * (b - a) / k))
  return mix(b, a, h) - k * h * (1.0 - h)

def circle(x, y, pos, rad):
  return length(sub(pos, (x, y))) - rad

def orbit1(x, y, t, pos):
  k = 0.1
  dist = 4.0 * (2.0 + t)
  ang = 10.0 * t / (2.0 * math.pi)
  return smin(
    circle(x, y, pos, 0.0),
    circle(x, y, sub(pos, muls((math.cos(ang), math.sin(ang)), dist)), 0),
    k)

def orbit2(x, y, t, pos):
  k = 0.1
  dist = 4.0 * (2.0 + t)
  ang = 10.0 * t / (2.0 * math.pi)
  return smin(
    circle(x, y, add(pos, muls((math.cos(ang), math.sin(ang)), dist)), 0),
    circle(x, y, sub(pos, muls((math.cos(ang), math.sin(ang)), dist)), 0),
    k)

def dist(x, y, t):
  #d = circle(x, y, (42.5, 3.5), 0.0)   # Point in the centre of the display
  d = orbit2(x, y, t, (41.5, 3.5))
  return 0 if math.modf(d * 0.1)[0] <= 0.5 else 1

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
  return base64.b64encode(bytearray(buffer))

def frame(t):
  grid = []
  
  for y in range(8):
    row = []
    for x in range(84):
      row.append(dist(x, y, t))
    grid.append(row)
  
  return encode(grid)

for t in range(360):
  f = frame(0.1 * t)
  decode.output(f)
  time.sleep(0.1)
