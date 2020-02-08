#de frente
#pin 1 -> 3.3v
#pin 2 -> GPIO23(pin 16)
#pin 2 -> 10Kohm -> 3.3v
#pin 3 -> nada
#pin 4 -> GND

import board
import adafruit_dht
import time

dht = adafruit_dht.DHT22(board.D23)

while True:
    try:
        print("Temperatura={0:0.1f}*C Humedad={1:0.1f}%".format(dht.temperature, dht.humidity))
    except Exception as err:
        print("Error:", err)
    time.sleep(2.0)

