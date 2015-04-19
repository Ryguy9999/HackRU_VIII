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
            #Accelerate
            if cmd == "A":
                ship.accelerate()
            #Brake
            elif cmd == "B":
                ship.brake()
            #Reverse
            elif cmd == "R":
                ship.reverse()
            #Izquireda- Left
            elif cmd == "I":
                ship.left()
            #Derecha- Right
            elif cmd == "D":
                ship.right()
        clock.tick(60)
        ship.update()
        display.blit(backRect, (0, 0, 640, 480))
        display.blit(pygame.transform.rotozoom(shipTex, shipTex.rotation, 1), (ship.x, ship.y, shipTex.get_rect().width, shipTex.get_rect().height))
        pygame.display.flip()
