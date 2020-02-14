import sys
import paho.mqtt.client as mqtt
import random
import time

def on_connect(client, userdata, flags, rc):
    print("Conectado al servidor mqtt");
    client.subscribe("sensor/pub")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.50.105", 1883, 60)

client.loop_start()

while True:
    try:
        rnd = random.random()
        print("Enviando " + str(rnd))
        client.publish("sensor/random", rnd)
        time.sleep(1.0)
    except KeyboardInterrupt:
        sys.exit();

