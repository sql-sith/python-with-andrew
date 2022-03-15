import position


class Character:

    def __init__(self, name="Default NPC", height=0, width=0, pos=position.Position()):
        self.name = name
        self.height = height
        self.width = width
        self.position = pos

    def move(self, dx, dy, maxX=None, maxY=None):
        """ Moves the character's location with optional bounds """
        if maxX is None:
            self.position.x += dx
            self.position.y += dy
        else:
            # Move x coordinate with bounds
            if self.position.x + dx - self.width < 0:
                self.position.x = 0 + self.width
            elif self.position.x + dx + self.width > maxX:
                self.position.x = maxX - self.width - 1
            else:
                self.position.x += dx
            # Move y coordinate with bounds
            if self.position.y + dy - self.height < 0:
                self.position.y = 0 + self.height
            elif self.position.y + dy + self.height > maxY:
                self.position.y = maxY - self.height - 1
            else:
                self.position.y += dy
