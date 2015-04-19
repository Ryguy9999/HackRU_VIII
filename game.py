import pygame, sys, random
from random import randrange
from pygame.locals import *
from ship import *
from Entity import Entity
from pew import Pew
commands = []
def rotate_center(image, angle, rect):
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
    (WIDTH, HEIGHT) = (800, 600)
    pygame.init()
    font = pygame.font.SysFont(None, 32)
    pygame.mixer.init()
    pew = pygame.mixer.Sound("pewpew.wav")
    pewTex = pygame.image.load("pew.png")
    asteroidTex = pygame.image.load("asteroid.png")
    labelNumber = font.render("NUMBER: 609-722-7113", 1, (85, 215, 200))
    labelA = font.render("A: Accelerate", 1, (85, 215, 200))
    labelR = font.render("R: Reverse", 1, (85, 215, 200))
    labelB = font.render("B: Brake", 1, (85, 215, 200))
    labelI = font.render("I: Left", 1, (85, 215, 200))
    labelD = font.render("D: Right", 1, (85, 215, 200))
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    shipTex = pygame.image.load("spaceship.png")
    ship = Ship(0, 0, shipTex.get_rect().width, shipTex.get_rect().height)
    ship.velocity = 1
    back = pygame.image.load("back.png")
    backRect = tile(back, WIDTH, HEIGHT)
    asteroids = []
    pews = []
    for j in range(1, 5):
        size = randrange(15, 50)
        asteroids.append(Entity(randrange(1, WIDTH), randrange(1, HEIGHT), size, size, randrange(2, 4), randrange(1, 360)))
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
        for asteroid in asteroids:
            asteroid.update()
            wrap(asteroid, WIDTH, HEIGHT)
        for pew in pews:
            pew.update()
            for asteroid in asteroids:
                if pew.collides(asteroid):
                    asteroids.remove(asteroid)
                    if asteroid.width > 20:
                        size = asteroid.width / 2 + random.randint(-3, 3)
                        asteroids.add(Entity(asteroid.x + random.randint(-5, 5), asteroid.y + random.randint(-5, 5), size, size, random.randint(3, 5), random.randint(1, 360)))
                        size = asteroid.width / 2 + random.randint(-3, 3)
                        asteroids.add(Entity(asteroid.x + random.randint(-5, 5), asteroid.y + random.randint(-5, 5), size, size, random.randint(3, 5), random.randint(1, 360)))
            if pew.lifetime <= 0:
                pews.remove(pew)
        while not commandsQueue.empty():
            cmd = commandsQueue.get()
            #Accelerate
            if cmd == "A" or cmd == 'a':
                ship.accelerate()
            #Brake
            elif cmd == "B" or cmd == 'b':
                    ship.brake()
            #Reverse
            elif cmd == "R" or cmd == 'r':
                    ship.reverse()
            #Izquireda- Left
            elif cmd == "I" or cmd == 'i':
                    ship.left()
            #Derecha- Right
            elif cmd == "D" or cmd == 'd':
                    ship.right()
            #Shoot
            elif cmd == "S" or cmd == 's':
                pew.play()
                pews.append(Pew(ship.x + shipTex.get_rect().width / 2, ship.y + ship.Tex.get_rect().height / 2, pewTex.get_rect().width, pewTex.get_rect().height, 10, ship.rotation))
        clock.tick(60)
        ship.update()
        wrap(ship, WIDTH, HEIGHT)
        display.blit(backRect, (0, 0, WIDTH, HEIGHT))
        (img, rect) = rotate_center(shipTex, ship.rotation, pygame.Rect(ship.x, ship.y, shipTex.get_rect().width, shipTex.get_rect().height))
        display.blit(img, rect)
        display.blit(labelNumber, (0, 0))
        for pew in pews:
            (img, rect) = rotate_center(pewTex, pew.rotation, pygame.Rect(pew.x, pew.y, pew.width, pew.height))
            display.blit(img, rect)
        for asteroid in asteroids:
            (img, rect) = rotate_center(asteroidTex, asteroid.rotation, pygame.Rect(asteroid.x, asteroid.y, asteroid.width, asteroid.height))
            display.blit(img, rect)
        display.blit(labelNumber, (0, 0))
        display.blit(labelA, (0, 25))
        display.blit(labelB, (0, 50))
        display.blit(labelR, (0, 75))
        display.blit(labelI, (0, 100))
        display.blit(labelD, (0, 125))
        display.blit(img, rect)
        pygame.display.flip()
