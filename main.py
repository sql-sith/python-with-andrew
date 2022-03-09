# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import character
import position


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
    basicNpc = character.Character("Harold", 2, 1, position.Position(5, 5))
    print_grid(15, 10, basicNpc)

    basicNpc.move(2, -1, 15, 10)
    print_grid(15, 10, basicNpc)

    print("\n\n===== Bottom right =====")
    basicNpc.move(100, -100, 15, 10)
    print_grid(15, 10, basicNpc)

    print("\n\n===== Top right =====")
    basicNpc.move(100, 100, 15, 10)
    print_grid(15, 10, basicNpc)

    print("\n\n===== Bottom left =====")
    basicNpc.move(-100, -100, 15, 10)
    print_grid(15, 10, basicNpc)

    print("\n\n===== Top left =====")
    basicNpc.move(-100, 100, 15, 10)
    print_grid(15, 10, basicNpc)
