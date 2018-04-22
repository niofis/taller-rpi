#Sensor PIR HC-SR501
#Docs: https://www.mpja.com/download/31227sc.pdf
#Conexion:
#GND -> GND (Pin 6)
#OUTPUT -> GPIO 7 (Pin 26)
#VCC -> GPIO 5v (Pin 2)

import time
import wiringpi
import sys

PIR = 7

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIR, 0) #entrada

while True:
    try:
        if wiringpi.digitalRead(PIR) == 1:
            print "Intrusos!!!"
            while wiringpi.digitalRead(PIR) ==1:
                pass
        time.sleep(0.2)
    except KeyboardInterrupt:
        sys.exit()

