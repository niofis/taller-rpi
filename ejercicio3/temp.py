#de frente
#pin 1 -> 3.3v
#pin 2 -> GPIO23(pin 16)
#pin 2 -> 10Kohm -> 3.3v
#pin 3 -> nada
#pin 4 -> GND

import Adafruit_DHT
import wiringpi


wiringpi.wiringPiSetupGpio()

DHT = 23

while True:
    humedad, temperatura = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, DHT)   

    if humedad is not None and temperatura is not None:
        print "Temperatura={0:0.1f}*C Humedad={1:0.1f}%".format(temperatura, humedad)
    else:
        print "Error al leer sensor"

    wiringpi.delay(1000)

