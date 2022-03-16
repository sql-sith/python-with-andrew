import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self, name="Default NPC", height=0, width=0):
        super(Character, self).__init__()
        self.name = name
        self.surf = pygame.Surface((20, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def move(self, dx, dy, surface=None):
        """ Moves the character's location with optional bounds """
        self.rect.move_ip(dx, 0)
        self.rect.move_ip(0, dy)
        if surface is not None:
            if self.rect.left < surface.get_rect().left:
                self.rect.left = surface.get_rect().left
            if self.rect.right > surface.get_rect().right:
                self.rect.right = surface.get_rect().left
            if self.rect.bottom < surface.get_rect().bottom:
                self.rect.bottom = surface.get_rect().bottom
            if self.rect.top > surface.get_rect().top:
                self.rect.top = surface.get_rect().top
