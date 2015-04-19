import pygame, sys
from pygame.locals import *

def gameFunc():
    pygame.init()
    display = pygame.display.set_mode((640, 480), 0, 32)
    ship = pygame.image.load("spaceship.png")
    back = pygame.image.load("back.png")
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
        display.fill((0, 0, 0))
        display.blit(ship, (0, 0, 32, 32))
        pygame.display.flip()
gameFunc()
