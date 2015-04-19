import pygame, sys
from pygame.locals import *
from ship import *
commands = []
def tile(img, width, height):
    surface = pygame.Surface((width, height))
    for x in range(0, width / img.get_rect().width):
        for y in range(0, height / img.get_rect().height):
            surface.blit(img, (x * img.get_rect().width, y * img.get_rect().height, img.get_rect().width, img.get_rect().height))
    return surface
def gameFunc(commandsQueue):
    global commands
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((640, 480), 0, 32)
    shipTex = pygame.image.load("spaceship.png")
    ship = Ship(0, 0, shipTex.get_rect().width, shipTex.get_rect().height)
    ship.velocity = 1
    back = pygame.image.load("back.png")
    backRect = tile(back, 640, 480)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
        while not commandsQueue.empty():
            cmd = commandsQueue.get()
            if cmd == "A":
                ship.x = 0
            elif cmd == "B":
                print "B"
            elif cmd == "R":
                print "R"
            elif cmd == "I":
                print "I"
            elif cmd == "D":
                print "D"
        clock.tick(60)
        ship.update()
        display.blit(backRect, (0, 0, 640, 480))
        display.blit(shipTex, (ship.x, ship.y, shipTex.get_rect().width, shipTex.get_rect().height))
        pygame.display.flip()
