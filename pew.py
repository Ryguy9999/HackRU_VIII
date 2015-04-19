import math
from Entity import Entity
class Pew(Entity):
    def __init__(self, x, y, width, height, speed, rotation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = speed
        self.rotation = rotation
        self.lifetime = 100
    def update(self):
        self.lifetime = self.lifetime - 1
        self.x += math.cos(math.radians(self.rotation)) * self.velocity
        self.y -= math.sin(math.radians(self.rotation)) * self.velocity
