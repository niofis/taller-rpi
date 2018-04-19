import wiringpi

#inicializa la libreria WiringPi
wiringpi.wiringPiSetupGpio()

PIN = 18

#configura el PIN para funcionar como PWM
wiringpi.pinMode(PIN, wiringpi.GPIO.PWM_OUTPUT)

#PWM en modo de milisegundos
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

#parametros para configurar una frecuencia de 50Hz
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

while True:
    for pulse in range(50, 250, 1):
        wiringpi.pwmWrite(PIN, pulse)
        wiringpi.delay(10)
    for pulse in range(250, 50, -1):
        wiringpi.pwmWrite(PIN, pulse)
        wiringpi.delay(10)
                                                            

