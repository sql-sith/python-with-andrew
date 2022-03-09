class Position:

    def __init__(self, x=0, y=0, orientation='l'):
        self.x = x
        self.y = y
        self.orientation = orientation

    def __str__(self):
        return f"{self.x}, {self.y}, {self.orientation}"
