import math
MAX_SPEED = 6
MAX_REVERSE = -3
ACCELERATION = 2
ROTATION = 10
BRAKING = 1.0
REVERSE = 2
MAX_TURN = 5
class Ship:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rotation = 0
		self.velocity = 0
		self.target_rotation = 0
		self.delta_x = 0
		self.delta_y = 0
		self.stun_timer = 0

	def update(self):
		self.x += math.cos(math.radians(self.rotation)) * self.velocity
		self.y -= math.sin(math.radians(self.rotation)) * self.velocity
		if self.rotation < self.target_rotation:
			if self.rotation + 1 < self.target_rotation:
				self.rotation += MAX_TURN
			else:
				self.rotation = self.target_rotation
		elif self.rotation > self.target_rotation:
			if self.rotation - MAX_TURN > self.target_rotation:
				self.rotation -= MAX_TURN
			else:
				self.rotation = self.target_rotation

		if self.stun_timer <> 0:
			self.rotation += 15
			self.target_rotation = self.rotation
			self.stun_timer -= 1
		else:
			if self.delta_x > 0:
				if self.delta_x - 0.1 < 0:
					self.delta_x = 0;
				else:
					self.delta_x -= 0.1;
			elif self.delta_x < 0:
				if self.delta_x + 0.1 > 0:
					self.delta_x = 0;
				else:
					self.delta_x += 0.1;
			if self.delta_y > 0:
				if self.delta_y - 0.1 < 0:
					self.delta_y = 0;
				else:
					self.delta_y -= 0.1;
			elif self.delta_y < 0:
				if self.delta_y + 0.1 > 0:
					self.delta_y = 0;
				else:
					self.delta_y += 0.1;
		print str(self.delta_x) + " " + str(self.delta_y)
		self.x += self.delta_x
		self.y += self.delta_y

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
		self.target_rotation += ROTATION
		if self.target_rotation > 0:
			self.target_rotation -= 360

	def right(self):
		self.target_rotation -= ROTATION
		if self.target_rotation < 360:
			self.target_rotation += 360
