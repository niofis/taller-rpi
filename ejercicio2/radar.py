import pygame, wiringpi, math, os, time

TRIG = 23
ECHO = 24
SERVO = 18

ENTRADA = 0
SALIDA = 1

wiringpi.wiringPiSetupGpio()

#configura el pin para el servo
wiringpi.pinMode(SERVO, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

#configura los pines para el sensor sonico
wiringpi.pinMode(TRIG, SALIDA)
wiringpi.pinMode(ECHO, ENTRADA)

#configura pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

ANCHO = 600
ALTO = 600
size = [ANCHO, ALTO]
origen = [ANCHO /2, ALTO]
radio = ANCHO / 4

VERDE1 = (0, 64, 0)
VERDE2 = (0, 128, 0)

pantalla = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

pygame.display.set_caption('Pi Radar')


def leeDistancia():
    inicio = 0
    fin = 0
    wiringpi.digitalWrite(TRIG, 0)
    time.sleep(2*10**-6)
    wiringpi.digitalWrite(TRIG, 1)
    time.sleep(10*10**-6)
    wiringpi.digitalWrite(TRIG, 0)

    while wiringpi.digitalRead(ECHO) == 0:
        inicio = time.time()
    while wiringpi.digitalRead(ECHO) == 1:
        fin = time.time()

    duracion = (fin - inicio) * 10**6
    distancia = duracion / 58
    return distancia

done = False
clock = pygame.time.Clock()

grados = 0
delta_grados = 2
ufos = []

#ciclo principal
while not done:
    #limite de 30 FPS
    # clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    #dibuja radar
    pantalla.fill(VERDE1)
    pygame.draw.line(pantalla, VERDE2, origen, [0, 0], 5)
    pygame.draw.line(pantalla, VERDE2, origen, [ANCHO, 0], 5)

    for i in range(1,5):
        pygame.draw.circle(pantalla, VERDE2, origen, radio * i, 5)

    #dibuja linea de seguimiento
    cos = math.cos(grados*math.pi/180)
    sen = math.sin(grados*math.pi/180)
    pygame.draw.line(pantalla, VERDE2, origen,
            [origen[0] + cos * ANCHO, origen[1] - sen * ALTO], 5);

    for ufo in ufos:
        pygame.draw.circle(pantalla, VERDE2, ufo['pos'], ufo['radio'])
        ufo['radio'] = ufo['radio'] - 1
        if ufo['radio'] == 0:
            ufos.remove(ufo)

    wiringpi.pwmWrite(SERVO, grados + 50)
    wiringpi.delay(10)

    distancia = leeDistancia()

    if distancia < 200:
        distancia = distancia * 5
        ufos.append({
            'pos':[
                int(origen[0] + cos * distancia),
                int(origen[1] - sen * distancia)],
            'radio': 50 })

    grados = grados + delta_grados

    if grados <= 0 or grados >= 180:
        delta_grados = -delta_grados

    pygame.display.flip()

pygame.quit()
