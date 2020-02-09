#Relay digital
# VCC -> 3.3V (Pin 1)
# GND -> Ground (Pin 6)
# IN -> GPIO 23 (Pin 16)

import time
import board
import digitalio

relay = digitalio.DigitalInOut(board.D23)
relay.direction = digitalio.Direction.OUTPUT

while True:
    relay.value = True
    time.sleep(1.0)
    relay.value = False
    time.sleep(1.0)
