'''

@author: Alex Berman
'''
import math

class Entity:
    def __init__(self, x, y, big, speed, rotation, width, height):
        self.x = x
        self.y = y
        self.big = big
        self.velocity = speed
        self.rotation = rotation
        self.width = width
        self.height = height

    def update(self):
		self.x += math.cos(math.radians(self.rotation)) * self.velocity
		self.y -= math.sin(math.radians(self.rotation)) * self.velocity

    def collides(self, obj):
		return not (self.x + self.width < obj.x or obj.x + obj.width < self.x or self.y + self.height < obj.y or obj.y + obj.height < self.y)
