# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import character


def print_grid(w, h, char=None):
    print("_" * (w + 2))
    for i in range(h):
        print("|", end='')
        for j in range(w):
            if char is not None and char.position.x - char.width <= j <= char.position.x + char.width \
                    and char.position.y - char.height <= h-i-1 <= char.position.y + char.height:
                print('X', end='')
            else:
                print('.', end='')
        print("|")
    print("-" * (w + 2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # basicNpc = character.Character("Harold", 2, 1, position.Position(5, 5))
    # print_grid(15, 10, basicNpc)
    #
    # basicNpc.move(2, -1, 15, 10)
    # print_grid(15, 10, basicNpc)
    #
    # print("\n\n===== Bottom right =====")
    # basicNpc.move(100, -100, 15, 10)
    # print_grid(15, 10, basicNpc)
    #
    # print("\n\n===== Top right =====")
    # basicNpc.move(100, 100, 15, 10)
    # print_grid(15, 10, basicNpc)
    #
    # print("\n\n===== Bottom left =====")
    # basicNpc.move(-100, -100, 15, 10)
    # print_grid(15, 10, basicNpc)
    #
    # print("\n\n===== Top left =====")
    # basicNpc.move(-100, 100, 15, 10)
    # print_grid(15, 10, basicNpc)
    # Simple pygame program

    # Import and initialize the pygame library
    import pygame

    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([1280, 720])

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
