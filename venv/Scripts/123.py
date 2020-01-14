import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
box = pygame.Rect(10,10,50,50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    box.x += 1
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 150, 255),box)
    pygame.display.flip()