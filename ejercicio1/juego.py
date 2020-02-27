import time
import sys
import board
import digitalio
import random


boton = digitalio.DigitalInOut(board.D17)
boton.direction = digitalio.Direction.INPUT
boton.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT


def esperaClic():
    time.sleep(0.1)
    while boton.value == True:
        pass
    time.sleep(0.1)
    while boton.value == False:
        pass

def jugar():
    #obtiene un numero aleatorio entre 1 y 6
    espera = random.uniform(1, 6)
    led.value = False
    #mantiene el led apagado por N milisegundos
    time.sleep(espera)
    led.value = True
    #guarda la hora en que se encendio el led
    inicio = time.time()
    while boton.value == True:
        #guarda la hora en que se presiono el boton
        fin = time.time()
    duracion = (fin - inicio)
    print("Tardaste ", duracion * 1000, "ms")
    time.sleep(1.0)


print("Para jugar haz clic y presiona de nuevo cuando se encienda el LED")

while True:
    try:
        led.value = True
        esperaClic()
        jugar()
    except KeyboardInterrupt:
        sys.exit()

