#Sensor HC-SR04
#Docs: http://www.micropik.com/PDF/HCSR04.pdf
#Connection:
#GND -> GND (Pin 6)
#ECHO -> 1Kohm -> GPIO 24 (Pin 18) -> 2Kohm -> GND
#TRIG -> GPIO -> 23 (Pin 16)
#VCC -> GPIO 5v (Pin 2)

import time
import wiringpi
import sys

TRIG = 23
ECHO = 24

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(TRIG, 1) #output
wiringpi.pinMode(ECHO, 0) #input

while True:
    try:
        wiringpi.digitalWrite(TRIG, 0)
        time.sleep(2*10**-6)
        wiringpi.digitalWrite(TRIG, 1)
        time.sleep(10*10**-6)
        wiringpi.digitalWrite(TRIG, 0)

        while wiringpi.digitalRead(ECHO) == 0:
            startTime = time.time()

        while wiringpi.digitalRead(ECHO) == 1:
            endTime = time.time()

        duration = (endTime - startTime) * 10**6
        distance = duration / 58

        print "Distance:", round(distance, 4), "cm"
        time.sleep(0.2)
    except KeyboardInterrupt:
        sys.exit()

