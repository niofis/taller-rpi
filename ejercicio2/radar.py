import pygame, wiringpi, math, os, time

TRIG = 23
ECHO = 24
SERVO = 18

INPUT = 0
OUTPUT = 1

wiringpi.wiringPiSetupGpio()

#servo cofiguration
wiringpi.pinMode(SERVO, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

#sonic sensor configuration
wiringpi.pinMode(TRIG, OUTPUT)
wiringpi.pinMode(ECHO, INPUT)

#pygame configuration
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

WIDTH = 600
HEIGHT = 600
size = [WIDTH, HEIGHT]
origin = [WIDTH /2, HEIGHT]
radius = WIDTH / 4

GREEN1 = (0, 64, 0)
GREEN2 = (0, 128, 0)

screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

pygame.display.set_caption('Pi Radar')


def readDistance():
    startTime = 0
    endTime = 0
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
    return distance

done = False
clock = pygame.time.Clock()

degrees = 0
delta_degrees = 2
ufos = []

#main loop
while not done:
    #30 FPS limit
    #clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    #draw radar
    screen.fill(GREEN1)
    pygame.draw.line(screen, GREEN2, origin, [0, 0], 5)
    pygame.draw.line(screen, GREEN2, origin, [WIDTH, 0], 5)

    for i in range(1,5):
        pygame.draw.circle(screen, GREEN2, origin, radius * i, 5)

    #draw radar line
    cos = math.cos(degrees*math.pi/180)
    sen = math.sin(degrees*math.pi/180)
    pygame.draw.line(screen, GREEN2, origin,
            [origin[0] + cos * WIDTH, origin[1] - sen * HEIGHT], 5);

    for ufo in ufos:
        pygame.draw.circle(screen, GREEN2, ufo['pos'], ufo['radius'])
        ufo['radius'] = ufo['radius'] - 1
        if ufo['radius'] == 0:
            ufos.remove(ufo)

    wiringpi.pwmWrite(SERVO, degrees + 50)
    wiringpi.delay(10)

    distance = readDistance()

    if distance < 200:
        distance = distance * 5
        ufos.append({
            'pos':[
                int(origin[0] + cos * distance),
                int(origin[1] - sen * distance)],
            'radius': 50 })

    degrees = degrees + delta_degrees

    if degrees <= 0 or degrees >= 180:
        delta_degrees = -delta_degrees

    pygame.display.flip()

pygame.quit()
