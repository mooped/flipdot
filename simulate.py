import paho.mqtt.client as mqtt

import decode

channels = [
  "nh/flipdot/comfy/buffer",
  "nh/flipdot/comfy/text",
  "nh/flipdot/comfy/raw",
  "nh/flipdot/comfy/brightness",
]

def on_subscribe(client, userdata, mid, reason_code_list, properties):
  for reason_code in reason_code_list:
    if reason_code_list[0].is_failure:
      print(f"Broker rejected you subscription: {reason_code}")
    else:
      print(f"Broker granted the following QoS: {reason_code.value}")

def on_unsubscribe(client, userdata, mid, reason_code_list, properties):
  # Be careful, the reason_code_list is only present in MQTTv5.
  # In MQTTv3 it will always be empty
  if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
    print("unsubscribe succeeded (if SUBACK is received in MQTTv3 it success)")
  else:
    print(f"Broker replied with failure: {reason_code_list[0]}")
  client.disconnect()

def on_message(client, userdata, message):
  if message.topic == "nh/flipdot/comfy/buffer":
    print("BUFFER:", message.payload)
  elif message.topic == "nh/flipdot/comfy/text":
    print("DISPLAY:", message.payload)
  elif message.topic == "nh/flipdot/comfy/raw":
    decode.output(message.payload)
  elif message.topic == "nh/flipdot/comfy/brightness":
    print("BRIGHTNESS:", message.payload)
  else:
    print("UNKNOWN: TOPIC", message.topic, "PAYLOAD", message.payload)

def on_connect(client, userdata, flags, reason_code, properties):
  if reason_code.is_failure:
    print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
  else:
    for channel in channels:
      client.subscribe(channel)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

mqttc.user_data_set([])
mqttc.connect("localhost")
mqttc.loop_forever()

