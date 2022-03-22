# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import game

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 780


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g = game.Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    g.begin_game_loop()
