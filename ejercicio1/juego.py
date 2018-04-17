import wiringpi, random, time

#iniciar la libreria WiringPi
wiringpi.wiringPiSetupGpio()

ENTRADA = 0
SALIDA = 1
PULLUP = 2
LED = 4
BOTON = 17

#configurar los pines
wiringpi.pinMode(LED, SALIDA)
wiringpi.pinMode(BOTON, ENTRADA)
wiringpi.pullUpDnControl(BOTON, PULLUP)

def esperaClic():
    wiringpi.delay(100)
    while wiringpi.digitalRead(BOTON) == 1:
        pass
    wiringpi.delay(100)
    while wiringpi.digitalRead(BOTON) == 0:
        pass

def jugar():
    #obtiene un numero aleatorio entre 1000 y 6000
    espera = random.randint(1000, 6000)
    wiringpi.digitalWrite(LED, 0)
    #mantiene el led apagado por N milisegundos
    wiringpi.delay(espera)
    wiringpi.digitalWrite(LED, 1)
    estado = wiringpi.digitalRead(BOTON)
    #guarda la hora en que se encendio el led
    inicio = time.time()
    while wiringpi.digitalRead(BOTON) == 1:
        #guarda la hora en que se presiono el boton
        fin = time.time()
    duracion = (fin - inicio)
    print "Tardaste ", duracion * 1000, "ms"

print "Para jugar haz clic y presiona de nuevo cuando se encienda el LED"

while True:
    wiringpi.digitalWrite(LED, 1)
    esperaClic()
    jugar()

