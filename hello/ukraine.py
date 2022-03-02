import random

# # numbers don't need quotes:
# print(32)
#
# # strings needs quotes:
# print('Hello, this is a sentence.')
# print('32')
#
# # difference between strings and numbers:
# print(32 + 5)
# print('32 + 5')
#
# # python loves indentation:
# food = "pizza"
#
# if food == "pizza":
#     print('Order more!')
# else:
#     print('Order pizza, please!')
#
# for i in range(-10, 10):
#     dollar_string = 'dollars'
#
#     if i == 1:
#         dollar_string = 'dollar'
#
#     print(f'I have a net worth of {i} {dollar_string}.')

# andrew loves diamonds:
diamond_number = random.randint(0, 64)

if diamond_number >= 32:
    print (f'{diamond_number} is a lot of diamonds.')
else:
    print(f'Only poor people have {diamond_number} diamond(s).')
