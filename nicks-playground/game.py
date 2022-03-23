import character
import pygame


FPS = 50
BORDER = 50


class Game:
    def __init__(self, screen_width: int, screen_height: int):
        """Constructor for Game class, which controls the looping of the game.

        :param screen_width: Width of screen viewport
        :param screen_height: Height of screen viewport
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = pygame.image.load("C:\\users\\nick\\pictures\\game_assets\\basic-stripe.png")
        self.background_width = self.background.get_size()[0]
        self.background_height = self.background.get_size()[1]
        print(self.background_width, self.background_height)
        self.viewport_corner_x = (self.background_width // 2) - (self.screen_width // 2)
        self.viewport_corner_y = (self.background_height // 2) - (self.screen_height // 2)
        print(self.viewport_corner_x, self.viewport_corner_y)
        self.player = character.Character("Cage", 50, 30,
                                          self.viewport_corner_x + self.screen_width // 2,
                                          self.viewport_corner_y + self.screen_height // 2)
        print(self.player.rect.top, self.player.rect.height)

    def begin_game_loop(self):
        """Does the work of running the game loop.

        :return: None
        """
        pygame.init()
        clock = pygame.time.Clock()
        # Set up the drawing window
        screen = pygame.display.set_mode([self.screen_width, self.screen_height])

        # Run until the user asks to quit
        running = True
        while running:
            self.update_assets(screen)
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(FPS)

        # Done! Time to quit.
        pygame.quit()
        print("Bye bye Cage!")

    def update_assets(self, screen):
        # Fill the background with black
        screen.fill((0, 0, 0))

        keys = pygame.key.get_pressed()
        self.player.update(keys, self.background_width, self.background_height)
        # print(self.player.rect.left, self.viewport_corner_x, self.screen_width)
        # Now we try to move the background based upon player movement
        # check if player has moved to the right past 20% from right side
        if self.player.rect.left + self.player.rect.width > self.viewport_corner_x + round(.8 * self.screen_width):
            # player left x + width > viewport corner left x + 80% screen width
            self.viewport_corner_x += self.player.speed
        # check if the player has moved to the left past 20% from the left side
        elif self.player.rect.left < self.viewport_corner_x + round(.2 * self.screen_width):
            # player left x < viewport corner left x + 20% screen width
            self.viewport_corner_x -= self.player.speed
        # ensure the viewport x is valid
        if self.viewport_corner_x > self.background_width + 2*BORDER - self.screen_width:
            self.viewport_corner_x = self.background_width + 2*BORDER - self.screen_width
        if self.viewport_corner_x < 0:
            self.viewport_corner_x = 0

        # check if player has moved up past 20% from top
        if self.player.rect.top - self.player.rect.height < self.viewport_corner_y + round(.2 * self.screen_height):
            self.viewport_corner_y -= self.player.speed
        # check if the player has down past 20% from bottom
        elif self.player.rect.top > self.viewport_corner_y + round(.8 * self.screen_height):
            self.viewport_corner_y += self.player.speed
        # ensure the viewport y is valid
        if self.viewport_corner_y > self.background_height + 2 * BORDER - self.screen_height:
            self.viewport_corner_y = self.background_height + 2 * BORDER - self.screen_height
        if self.viewport_corner_y < 0:
            self.viewport_corner_y = 0

        screen.blit(self.background, (BORDER - self.viewport_corner_x, BORDER - self.viewport_corner_y))
        screen.blit(self.player.image, (BORDER + self.player.rect.left - self.viewport_corner_x,
                    BORDER + self.player.rect.top - self.viewport_corner_y))
        # Flip the display
        pygame.display.flip()


