import base64
import math
import random
import sys

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

"""
def smin(a, b, k):
  h = max(0.0, min(1.0, 0.5 + 0.5 * (b - a) / k))
  return self.mix(b, a, h) - k * h * (1.0 - h)
"""

def circle(x, y, pos, rad):
  return length(sub(pos, (x, y))) - rad

"""
def orbit(self, pos):
  const float k = 0.1;
  const vec2 pos = vec2(0.75, 0.5);
  float dist = 0.1 * (2.0 + sin(iTime));
  float ang = iTime / (2.0 * PI);
  return smin(
      circle(uv - pos, 0.0),
      circle(uv - pos - dist * vec2(cos(ang), sin(ang)), 0.0),
      k);
"""

def dist(x, y):
  d = circle(x, y, (42.5, 3.5), 0.0)   # Point in the centre of the display
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

grid = []

for y in range(8):
  row = []
  for x in range(84):
    row.append(dist(x, y))
  grid.append(row)

decode.output(encode(grid))

