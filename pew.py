import Entity
class Pew(Entity):
    def __init__(self, x, y, width, height, speed, rotation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.rotation = rotation
        self.lifetime = 1000
    def update(self):
		self.x += math.cos(math.radians(self.rotation)) * self.velocity
		self.y -= math.sin(math.radians(self.rotation)) * self.velocity
        self.lifetime -= 1
