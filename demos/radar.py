import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
size = [WIDTH, HEIGHT]
origin = [WIDTH /2, HEIGHT]
radius = WIDTH / 4

BACKGROUND = (0, 64, 0)
FOREGROUND = (0, 128, 0)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Pi Radar')

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BACKGROUND)
    pygame.draw.line(screen, FOREGROUND, [0, 0], origin, 5)
    pygame.draw.line(screen, FOREGROUND, [WIDTH, 0], origin, 5)

    for i in range(1,5):
        pygame.draw.circle(screen, FOREGROUND, origin, radius * i, 5)


    pygame.display.flip()

pygame.quit()
