import pygame, sys
from pygame.locals import *
from ship import *
commands = []
def rot_center(image, angle, rect):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotozoom(image, angle, 1)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect
def tile(img, width, height):
    surface = pygame.Surface((width, height))
    for x in range(0, width / img.get_rect().width):
        for y in range(0, height / img.get_rect().height):
            surface.blit(img, (x * img.get_rect().width, y * img.get_rect().height, img.get_rect().width, img.get_rect().height))
    return surface
def wrap(rect, width, height):
    if rect.x < 0:
        rect.x = width + rect.x
    if rect.y < 0:
        rect.y = height + rect.y
    if rect.x > width:
        rect.x = width - rect.x
    if rect.y > height:
        rect.y = height - rect.y
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
        wrap(ship, 640, 480)
        display.blit(backRect, (0, 0, 640, 480))
        display.blit(rotate_center(shipTex, ship.rotation, (ship.x, ship.y, shipTex.get_rect().width, shipTex.get_rect().height)))
        pygame.display.flip()
