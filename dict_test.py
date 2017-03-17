
print('Enter player 1\'s jersey number:')

print('Enter player 1\'s rating:\n')


print('Enter player 2\'s jersey number:')

print('Enter player 2\'s rating:\n')


print('Enter player 3\'s jersey number:')

print('Enter player 3\'s rating:\n')


print('Enter player 4\'s jersey number:')

print('Enter player 4\'s rating:\n')

print('Enter player 5\'s jersey number:')

print('Enter player 5\'s rating:\n')

player_dict={84: 7, 23: 4, 4: 5, 30: 2, 66: 9}
player_list = [(k, v) for k, v in dict.items(player_dict)]

for jersey, rating in sorted(player_list):
    print('Player number: {:3d}   Rating: {:2d}'.format(jersey, rating))
jersey = int((input("Enter player's jersey number:\n")))
rating = int((input("Enter player's rating:\n")))
player_dict.setdefault(jersey, rating)
