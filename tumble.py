import argparse
import base64
import math
import paho.mqtt.client as mqtt
import random
import subprocess
import sys
import time

import decode
import font

parser = argparse.ArgumentParser(prog="Hexate",description="Flipdot Distance Field Renderer")
parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()

message = None

def on_message(client, userdata, msg):
    global message
    print(msg.topic + " " + str(msg.payload))
    message = msg.payload.decode()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_message = on_message
mqttc.connect('localhost')
mqttc.loop_start()

mqttc.subscribe('nh/flipdot/comfy/text')

def set_buffer(index):
  mqttc.publish('nh/flipdot/comfy/buffer', index)

def send_raw(message):
  mqttc.publish('nh/flipdot/comfy/raw', message)

def send_text(message):
  mqttc.publish('nh/flipdot/comfy/text', message)

for i in range(600):
  if message:
    break
  time.sleep(0.5)
  print("...")

if not message:
  sys.exit(0)

time.sleep(1)

grid = []
for y in range(8):
  grid.append([0] * 84)

font.grid = grid
font.drawText(font.font5x7Fixed, 0, 0, message, 1, 0, 1, 1)
grid.reverse()

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

set_buffer(8)

for _ in range(8):
  m = encode(grid)
  send_raw(m)
  if args.verbose:
    decode.output(m)
  grid = grid[1:]
  time.sleep(0.5)

time.sleep(10)
send_text("OOPS!")

time.sleep(10)
set_buffer(0)

mqttc.loop_stop()

