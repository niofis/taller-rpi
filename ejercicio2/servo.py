import wiringpi

#initialize WiringPi library
wiringpi.wiringPiSetupGpio()

PIN = 18

#setup PIN to work as pwm output
wiringpi.pinMode(PIN, wiringpi.GPIO.PWM_OUTPUT)

#set PWM mode to milliseconds
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

#50Hz configuration
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

while True:
    for pulse in range(50, 250, 1):
        wiringpi.pwmWrite(PIN, pulse)
        wiringpi.delay(10)
    for pulse in range(250, 50, -1):
        wiringpi.pwmWrite(PIN, pulse)
        wiringpi.delay(10)
                                                            

