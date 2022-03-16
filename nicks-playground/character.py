import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self, name="Default NPC", height=50, width=30, speed=1):
        super(Character, self).__init__()
        self.name = name
        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.image = pygame.image.load("C:\\users\\nick\\pictures\\game_assets\\tiny_cage.png")
        self.speed = speed

    def move(self, dx, dy, min_x=None, max_x=None, min_y=None, max_y=None):
        """ Moves the character's location with optional bounds """
        self.rect.move_ip(dx, 0)
        self.rect.move_ip(0, dy)
        if min_x is not None and max_x is not None and min_y is not None and max_y is not None:
            if self.rect.left < min_x:
                self.rect.left = min_x
            if self.rect.right > max_x:
                self.rect.right = max_x
            if self.rect.bottom > max_y:
                self.rect.bottom = max_y
            if self.rect.top < min_y:
                self.rect.top = min_y

    def update(self, keys, screen_width, screen_height):
        # Update speed first
        if keys[pygame.K_KP_PLUS]:
            self.speed = min (self.speed + 1, 10)
        if keys[pygame.K_KP_MINUS]:
            self.speed = max(self.speed - 1, 1)

        # Update position
        if keys[pygame.K_w]:
            self.move(0, -self.speed, 0, screen_width, 0, screen_height)
        if keys[pygame.K_a]:
            self.move(-self.speed, 0, 0, screen_width, 0, screen_height)
        if keys[pygame.K_s]:
            self.move(0, self.speed, 0, screen_width, 0, screen_height)
        if keys[pygame.K_d]:
            self.move(self.speed, 0, 0, screen_width, 0, screen_height)
