import pygame, sys
from pygame.locals import *
commands = []
def tile(img, width, height):
    surface = pygame.Surface((width, height))
    for x in range(0, width / img.get_rect().width):
        for y in range(0, height / img.get_rect().height):
            surface.blit(img, (x * img.get_rect().width, y * img.get_rect().height, img.get_rect().width, img.get_rect().height))
    return surface
def gameFunc():
    pygame.init()
    display = pygame.display.set_mode((640, 480), 0, 32)
    ship = pygame.image.load("spaceship.png")
    back = pygame.image.load("back.png")
    backRect = tile(back, 640, 480)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
        display.blit(backRect, (0, 0, 640, 480))
        display.blit(ship, (0, 0, 32, 32))
        pygame.display.flip()
gameFunc()
