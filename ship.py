class Ship:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	def collides(self, obj):
		return not (self.x + self.width < obj.x or obj.x + obj.width < self.x or self.y + self.height < obj.y or obj.y + obj.height < self.y)