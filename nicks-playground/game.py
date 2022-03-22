import character
import pygame


class Game():
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player = character.Character("Cage", 50, 30, 3)
        self.background = pygame.image.load("C:\\users\\nick\\pictures\\game_assets\\basic-stripe.png")
        self.viewport_corner_x = (self.background.get_size()[0] // 2) - (self.screen_width // 2)
        self.viewport_corner_y = (self.background.get_size()[1] // 2) - (self.screen_height // 2)

    def begin_game_loop(self):
        pygame.init()
        clock = pygame.time.Clock()
        # Set up the drawing window
        screen = pygame.display.set_mode([self.screen_width, self.screen_height])



        # Run until the user asks to quit
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background with black
            screen.fill((0, 0, 0))

            screen.blit(self.player.image, self.player.rect)
            keys = pygame.key.get_pressed()
            self.player.update(keys, self.screen_width, self.screen_height)

            # Flip the display
            pygame.display.flip()
            clock.tick(50)

        # Done! Time to quit.
        pygame.quit()
        print("Bye bye Cage!")

    def updateAssets(self):
        print("TODO")


