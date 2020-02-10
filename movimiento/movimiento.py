#Sensor PIR HC-SR501
#Docs: https://www.mpja.com/download/31227sc.pdf
#Conexion:
#GND -> GND (Pin 6)
#OUTPUT -> GPIO 23 (Pin 16)
#VCC -> GPIO 5v (Pin 2)

import sys
import time
import board
import digitalio

pir = digitalio.DigitalInOut(board.D23)
pir.direction = digitalio.Direction.INPUT

while True:
    try:
        if pir.value == True:
            print("Intrusos!")
            while pir.value == True:
                pass
            print("Todo bien...")
        time.sleep(0.2)
    except KeyboardInterrupt:
        sys.exit()


