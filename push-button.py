# Leer el estado de un boton
# Configuración:
# Tierra PIN 6
# Boton PIN 17

import wiringpi, random, time

wiringpi.wiringPiSetupGpio()

ENTRADA = 0
SALIDA = 1
PULLUP = 2
BOTON = 17

wiringpi.pinMode(BOTON, ENTRADA)
wiringpi.pullUpDnControl(BOTON, PULLUP)

while True:
    if wiringpi.digitalRead(BOTON) == 0:
        print("CLICK!");
        while wiringpi.digitalRead(BOTON) == 0:
            wiringpi.delay(100);
