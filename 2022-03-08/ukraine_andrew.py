import random

# random.randint(0, 10)
#
# numbers = random.randint(1, 6), random.randint(1, 6)
# x, y = numbers
# print(x)
# print(y)
#
# print(y + x)
# rolls = random.randrange(0, 7)
# print(rolls)
# rolls = random.randint(1, 6)
typeDice = input('How many sides will your dice have?\n')
typeDice = int(typeDice)
print('Ok!')

rolls = input('How many dice do you want to roll?\n')
rolls = int(rolls)
highestRoll = rolls * typeDice
print(f'I have {rolls} dice')

rollsLeft = 0
finalCount = 0


def random_dice():
    roll_value = random.randint(1, typeDice)
    print(roll_value)
    return roll_value


while rollsLeft < rolls:
    finalCount += random_dice()
    rollsLeft += 1

if finalCount == 10:
    answer = input('Do you wish to continue? Y / N\n')
else:
    if finalCount <= highestRoll * 0.40:
        print(f'My total is {finalCount}. That\'s pretty low.')
        exit()
    else:
        print(f'My total is {finalCount}')
        exit()
if answer == 'N' or 'n':
    exit()
print('so be it')
