class Bullet:
    def __init__(self, x, y, direction):
        self.x_position = x
        self.y_position = y
        self.speed = 5
        self.direction = direction



    def update(self):
        self.y_position += self.speed * self.direction


