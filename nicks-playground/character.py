import pygame

MAX_SPEED = 10
MIN_SPEED = 1


class Character(pygame.sprite.Sprite):

    def __init__(self, name="Default NPC", height=50, width=30, left_x: int = 0, top_y: int  = 0, speed=1):
        """Basic Character constructor

        :param name: Name of character (default: "Default NPC")
        :param height: Height of character (default: 50)
        :param width: Width of character (default: 30)
        :param left_x: X of top left corner of character location (default: 0)
        :param top_y: Y of top left corner of character location (default: 0)
        :param speed: Speed of character (default: 1)
        """
        super(Character, self).__init__()
        self.name = name
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect()
        self.rect.left = left_x
        self.rect.top = top_y
        self.image = pygame.image.load("C:\\users\\nick\\pictures\\game_assets\\tiny_cage.png")
        self.speed = speed

    def move(self, dx: int, dy: int, min_x: int = None, max_x: int = None, min_y: int = None, max_y: int = None):
        """Moves the character.

        :param dx: Distance (in pixels) to move in x direction
        :param dy: Distance (in pixels) to move in y direction
        :param min_x: (optional) Minimum character x value
        :param max_x: (optional) Maximum character x value
        :param min_y: (optional) Minimum character y value
        :param max_y: (optional) Maximum character y value
        :return: None
        """
        self.rect.move_ip(dx, dy)
        if min_x is not None and max_x is not None and min_y is not None and max_y is not None:
            if self.rect.left < min_x:
                self.rect.left = min_x
            if self.rect.right > max_x:
                self.rect.right = max_x
            if self.rect.bottom > max_y:
                self.rect.bottom = max_y
            if self.rect.top < min_y:
                self.rect.top = min_y

    def update(self, keys, screen_width: int, screen_height: int):
        """Updates character based upon given key presses.

        :param keys: List of keys pressed, given by PyGame engine
        :param screen_width: Width of screen viewport
        :param screen_height: Height of screen viewport
        :return: None
        """
        # Update speed first
        if keys[pygame.K_KP_PLUS]:
            self.speed = min(self.speed + 1, MAX_SPEED)
        if keys[pygame.K_KP_MINUS]:
            self.speed = max(self.speed - 1, MIN_SPEED)
        # Update position
        if keys[pygame.K_w]:
            self.move(0, -self.speed, 0, screen_width, 0, screen_height)
        if keys[pygame.K_a]:
            self.move(-self.speed, 0, 0, screen_width, 0, screen_height)
        if keys[pygame.K_s]:
            self.move(0, self.speed, 0, screen_width, 0, screen_height)
        if keys[pygame.K_d]:
            self.move(self.speed, 0, 0, screen_width, 0, screen_height)
