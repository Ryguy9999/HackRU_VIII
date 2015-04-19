import math
MAX_SPEED = 6
MAX_REVERSE = -3
ACCELERATION = 2
ROTATION = 3
BRAKING = 0.1
REVERSE = 2
class Ship:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rotation = 0
		self.velocity = 0
	def update(self):
		self.x += math.cos(math.radians(self.rotation)) * self.velocity
		self.y -= math.sin(math.radians(self.rotation)) * self.velocity
	def collides(self, obj):
		return not (self.x + self.width < obj.x or obj.x + obj.width < self.x or self.y + self.height < obj.y or obj.y + obj.height < self.y)

	def accelerate(self):
		if self.velocity < MAX_SPEED:
			if self.velocity + ACCELERATION > MAX_SPEED:
				self.velocity = MAX_SPEED
			else:
				self.velocity += ACCELERATION

	def brake(self):
		if self.velocity > 0:
			if self.velocity - BRAKING < 0:
				self.velocity = 0
			else:
				self.velocity -= BRAKING
		elif self.velocity < 0:
			if self.velocity + BRAKING > 0:
				self.velocity = 0
			else:
				self.velocity += BRAKING

	def reverse(self):
		if self.velocity > MAX_REVERSE:
			if self.velocity - REVERSE < MAX_REVERSE:
				self.velocity = MAX_REVERSE
			else:
				self.velocity -= REVERSE

	def left(self):
		self.rotation -= ROTATION
		if self.rotation < 0:
			self.rotation += 360

	def right(self):
		self.rotation += ROTATION
		if self.rotation > 360:
			self.rotation -= 360
