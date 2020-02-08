#Sensor HC-SR04
#Docs: http://www.micropik.com/PDF/HCSR04.pdf
#Connection:
#GND -> GND (Pin 6)
#ECHO -> 1Kohm -> GPIO 24 (Pin 18) -> 2Kohm -> GND
#TRIG -> GPIO -> 23 (Pin 16)
#VCC -> GPIO 5v (Pin 2)

import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D23, echo_pin=board.D24)

while True:
    try:
        print(sonar.distance)
    except KeyboardInterrupt:
        sys.exit()
    except Exception as ex:
        print(ex)
    time.sleep(0.2)

