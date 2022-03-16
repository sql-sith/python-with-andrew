# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import character
import pygame


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 780


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()
    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    basicNpc = character.Character("Cage", 50, 30, 3)

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with black
        screen.fill((0, 0, 0))

        # Draw a solid blue circle in the center
        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        screen.blit(basicNpc.image, basicNpc.rect)
        keys = pygame.key.get_pressed()
        basicNpc.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        # basicNpc.move(random.randint(0, 1), random.randint(0, 1), 0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

        # Flip the display
        pygame.display.flip()
        clock.tick(50)

    # Done! Time to quit.
    pygame.quit()
    print("Bye bye Cage!")
