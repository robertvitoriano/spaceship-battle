class Bullet:
    def __init__(self, x, y):
        self.x_position = x
        self.y_position = y
        self.speed = 5

    def update(self):
        self.y_position -= self.speed


