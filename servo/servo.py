# Servo SG90
# Café -> GND (Pin 6)
# Rojo -> 5V (Pin 2)
# Amarillo -> GPIO 23 (Pin 16)
import RPi.GPIO as GPIO
import time
import sys

PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, 50)
servo.start(2.5)

# 2.5 -> 0 Grados
# 12.5 -> 180 Grados

while True:
    try:
        i = 2.5
        while i <= 12.5:
            servo.ChangeDutyCycle(i)
            time.sleep(0.01)
            i = i + 0.1
        i = 12.5
        while i >= 2.5:
            servo.ChangeDutyCycle(i)
            time.sleep(0.01)
            i = i - 0.1
    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
        sys.exit()
