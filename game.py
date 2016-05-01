import pygame, sys, random
from random import randrange, getrandbits
from pygame.locals import *
from ship import *
from Entity import Entity
from pew import Pew
from explosions import Explosion
commands = []
score = 0
(WIDTH, HEIGHT) = (5000, 5000)
(S_WIDTH, S_HEIGHT) = (800, 600)
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def rotate_center(image, angle, rect):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotozoom(image, angle, 1)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect
def tile(img, width, height):
    surface = pygame.Surface((width, height))
    for x in range(0, width / img.get_rect().width + 1):
        for y in range(0, height / img.get_rect().height + 1):
            surface.blit(img, (x * img.get_rect().width, y * img.get_rect().height, img.get_rect().width, img.get_rect().height))
    return surface
def wrap(rect, width, height, offset = (0, 0)):
    (x, y) = offset
    if rect.x < x + -rect.width / 2:
        rect.x = x + WIDTH
    if rect.y < y + -rect.height / 2:
        rect.y = y + HEIGHT
    if rect.x > x + WIDTH:
        rect.x = x
    if rect.y > y + HEIGHT:
        rect.y = y
def gameFunc(commandsQueue):
    global commands
    global score
    comSent = []
    pygame.init()
    font = pygame.font.SysFont(None, 32)
    pygame.mixer.init()
    pewSound = pygame.mixer.Sound("pewpew.wav")
    crunchSound = pygame.mixer.Sound("crunch.wav")
    pewTex = pygame.image.load("pew.png")
    fwoom = pygame.mixer.Sound("fwoom.wav")
    asteroidTex = pygame.image.load("asteroid.png")
    explosionTex = pygame.image.load("explosion.png")
    labelNumber = font.render("NUMBER: 609-722-7113", 1, (85, 215, 200))
    labelA = font.render("W: Accelerate", 1, (85, 215, 200))
    labelR = font.render("S: Reverse", 1, (85, 215, 200))
    labelB = font.render("B: Brake", 1, (85, 215, 200))
    labelI = font.render("A: Left", 1, (85, 215, 200))
    labelD = font.render("D: Right", 1, (85, 215, 200))
    labelS = font.render("F: Fire", 1, (85, 215, 200))
    clock = pygame.time.Clock()
    info = pygame.display.Info()
    (S_WIDTH, S_HEIGHT) = (800, 600)
    display = pygame.display.set_mode((S_WIDTH, S_HEIGHT), 0, 32)
    shipTex = pygame.image.load("spaceship.png")
    ship = Ship(0, 0, shipTex.get_rect().width, shipTex.get_rect().height)
    ship.target_rotation = 305
    ship.velocity = 0
    goalTex = pygame.image.load("goal.png")
    (goal_x, goal_y) = (WIDTH / 2, HEIGHT / 2)
    back = pygame.image.load("back.png")
    backRect = tile(back, WIDTH, HEIGHT)
    camera = Rect(0, 0, S_WIDTH, S_HEIGHT)
    asteroids = []
    pews = []
    explosions = []
    for j in range(1, 10):
        asteroids.append(Entity(randrange(1, WIDTH), randrange(1, HEIGHT), bool(random.getrandbits(1)), randrange(2, 4), randrange(1, 360), asteroidTex.get_rect().width, asteroidTex.get_rect().height))
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
        for asteroid in asteroids:
            asteroid.update()
            wrap(asteroid, S_WIDTH, S_HEIGHT, (camera.x, camera.y))
            if asteroid.collides(ship):
                ship.stun_timer = 60
                ship.delta_x = (ship.x - asteroid.x) / 16
                ship.delta_y = (ship.y - asteroid.y) / 16
                asteroids.remove(asteroid)
                score -= randrange(250, 500)
                crunchSound.play()
                explosions.append(Explosion(asteroid.x, asteroid.y))
            for asteroid2 in asteroids:
                if asteroid != asteroid2 and asteroid.collides(asteroid2):
                    asteroids.remove(asteroid)
                    asteroids.remove(asteroid2)
                    explosions.append(Explosion(asteroid.x, asteroid.y))
                    if asteroid.collides(camera):
                        crunchSound.play()
                    break
            if not asteroid in asteroids:
                break
        for explosion in explosions:
            if explosion.update():
                explosions.remove(explosion)
                continue
        if len(asteroids) < 40:
            size = randrange(15, 50)
            rect = Rect(randrange(1, WIDTH), randrange(1, HEIGHT), size, size)
            while camera.colliderect(rect):
                rect = Rect(randrange(1, WIDTH), randrange(1, HEIGHT), size, size)
            asteroids.append(Entity(rect.x, rect.y, bool(random.getrandbits(1)), randrange(2, 4), randrange(1, 360), asteroidTex.get_rect().width, asteroidTex.get_rect().height))
        for pew in pews:
            pew.update()
            wrap(pew, WIDTH, HEIGHT)
            for asteroid in asteroids:
                if pew.collides(asteroid):
                    asteroids.remove(asteroid)
                    pews.remove(pew)
                    crunchSound.play()
                    score += randrange(1000, 3000)
                    if asteroid.big:
                        asteroids.append(Entity(asteroid.x + random.randint(-5, 5), asteroid.y + random.randint(-5, 5), False, random.randint(3, 5), random.randint(1, 360), 32, 32))
                        asteroids.append(Entity(asteroid.x + random.randint(-5, 5), asteroid.y + random.randint(-5, 5), False, random.randint(3, 5), random.randint(1, 360), 32, 32))
                    break
            if pew.lifetime <= 0:
                pews.remove(pew)
        if goal_x != -1 and distance(ship.x + shipTex.get_rect().width / 2, ship.y + shipTex.get_rect().height /2, goal_x, goal_y) < 160:
            score += 100000
            goal_x = -1
            goal_y = -1
        while not commandsQueue.empty():
            cmd = commandsQueue.get()
            comSent.append(cmd.upper())
            #Accelerate
            if cmd == "W" or cmd == 'w':
                ship.accelerate()
                fwoom.play()
            #Brake
            elif cmd == "B" or cmd == 'b':
                    ship.brake()
            #Reverse
            elif cmd == "S" or cmd == 's':
                    ship.reverse()
            #Izquireda- Left
            elif cmd == "A" or cmd == 'a':
                    ship.left()
            #Derecha- Right
            elif cmd == "D" or cmd == 'd':
                    ship.right()
            #Shoot
            elif cmd == "F" or cmd == 'f':
                pewSound.play()
                pews.append(Pew(ship.x + shipTex.get_rect().width / 2, ship.y + shipTex.get_rect().height / 2, pewTex.get_rect().width, pewTex.get_rect().height, 10, ship.rotation))
        if len(comSent) > 10:
            comSent.remove(comSent[0])
        if ship.stun_timer > 0:
            camera.x = ship.x - S_WIDTH / 2
            camera.y = ship.y - S_HEIGHT / 2
        else:
            camera.x = camera.x + ((ship.x - S_WIDTH / 2) - camera.x) / 16
            camera.y = camera.y + ((ship.y - S_HEIGHT / 2) - camera.y) / 16
        if camera.x < 0:
            camera.x = 0
        elif camera.x + camera.width > WIDTH:
            camera.x = WIDTH - camera.width
        if camera.y < 0:
            camera.y = 0
        elif camera.y + camera.height > HEIGHT:
            camera.y = HEIGHT - camera.height
        ship.update()
        wrap(ship, WIDTH, HEIGHT)
        display.blit(backRect, (0, 0, WIDTH, HEIGHT), camera)
        (img, rect) = rotate_center(shipTex, ship.rotation, pygame.Rect(ship.x, ship.y, shipTex.get_rect().width, shipTex.get_rect().height))
        display.blit(img, (rect.x - camera.x, rect.y - camera.y, rect.width, rect.height))

        for pew in pews:
            (img, rect) = rotate_center(pewTex, pew.rotation, pygame.Rect(pew.x, pew.y, pew.width, pew.height))
            display.blit(img, (rect.x - camera.x, rect.y - camera.y, rect.width, rect.height))
        for asteroid in asteroids:
            (img, rect) = rotate_center(asteroidTex, asteroid.rotation, pygame.Rect(asteroid.x, asteroid.y, asteroidTex.get_rect().width, asteroidTex.get_rect().height))
            display.blit(img, (rect.x - camera.x, rect.y - camera.y, rect.width, rect.height))
        for explosion in explosions:
            display.blit(explosionTex, (explosion.x - camera.x, explosion.y - camera.y, explosionTex.get_rect().width, explosionTex.get_rect().height), explosion.get_piece())
        if goal_x != -1:
            display.blit(goalTex, (goal_x - camera.x, goal_y - camera.y, goalTex.get_rect().width, goalTex.get_rect().height))
        #Draw objective

        display.blit(labelNumber, (0, 0))
        display.blit(labelA, (0, 25))
        display.blit(labelB, (0, 50))
        display.blit(labelR, (0, 75))
        display.blit(labelI, (0, 100))
        display.blit(labelD, (0, 125))
        display.blit(labelS, (0, 150))
        labelScore = font.render("SCORE: " + str(score), 1, (85, 215, 200))
        display.blit(labelScore, (S_WIDTH - 400, 0))
        string = ""
        for item in comSent:
            string += item + " "
        labelComs = font.render("Commands: " + string, 1, (85, 215, 200))
        display.blit(labelComs, (S_WIDTH - 400, 50))
        pygame.display.flip()
        clock.tick(60)
