import sys
import paho.mqtt.client as mqtt
import random
import time

def on_connect(client, userdata, flags, rc):
    print("Conectado al servidor mqtt")
    client.subscribe("sensor/temperatura")
    client.subscribe("sensor/humedad")

def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode("UTF-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.50.105", 1883, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    sys.exit()

