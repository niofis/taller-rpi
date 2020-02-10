# Push button
# Tierra -> GND (PIN 6)
# Boton -> GPIO 23 (PIN 16)

import time
import sys
import board
import digitalio

button = digitalio.DigitalInOut(board.D23)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    try:
        if button.value == True:
            print("Click!")
            while button.value == True:
                time.sleep(0.2)
    except KeyboardInterrupt:
        sys.exit()
