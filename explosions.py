class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.next = 0
    def update(self):
        self.next += 1
        if self.next >= 5:
            self.next = 0
            self.frame += 1
        if self.frame > 6:
            return True
    def get_piece(self):
        return (self.frame * 32, 0, 32, 32)
