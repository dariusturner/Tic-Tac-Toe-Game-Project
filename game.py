# Tic Tac Toe Game - Written in Python by Darius Turner 2019

print('Thank you for playing Tic Tac Toe!')

x_or_o = input('Player 1: Would you like to be X or O?' + '\n')

print(x_or_o)

if x_or_o == 'X' or x_or_o == 'x':
    player1 = 'X'
    player2 = 'O'
    print("Player1 is X and player2 is O" + '\n')
elif x_or_o == 'O' or x_or_o == 'o':
    player1 = 'X'
    player2 = 'O'
    print("Player 1 is O and player2 is X" + '\n')
else:
    print('That option is unavaiable, please try again.' + '\n')

available_spaces = [1,2,3,4,5,6,7,8,9]

grid = ' | | ' + '\n' + f'{available_spaces[0]}|{available_spaces[1]}|{available_spaces[2]}' + '\n' + ' | | ' + '\n' + '------' + '\n' +' | | ' + '\n' + f'{available_spaces[3]}|{available_spaces[4]}|{available_spaces[5]}' + '\n' + ' | | ' + '\n' + '------' + '\n' + ' | | ' + '\n' + f'{available_spaces[6]}|{available_spaces[7]}|{available_spaces[8]}' + '\n' + ' | | ' + '\n'

print(grid + '\n')

choose_position  = input('Choose your position 1 - 9')

def player1_move(position):
    if position == 1 and available_spaces[0] != player2:
        available_spaces[0] = player1 
    elif position == 2 and available_spaces[1] != player2:
        available_spaces[1] = player1 
    elif position == 3 and available_spaces[2] != player2:
        available_spaces[2]  = player1
    elif position == 4 and available_spaces[3] != player2:
        available_spaces[3] = player1
    elif position == 5 and available_spaces[4] != player2:
        available_spaces[4] = player1
    elif position == 6 and available_spaces[5] != player2:
        available_spaces[5] = player1
    elif position == 7 and available_spaces[6] != player2:
        available_spaces[6] = player1
    elif position == 8 and available_spaces[7] != player2:
        available_spaces[7] = player1
    elif position == 9 and available_spaces[8] != player2:
        available_spaces[8] = player1
    else:
        input('Sorry that position is unavailable.' + '\n' + choose_position)

print(choose_position)            

player1_move(choose_position)

print(grid)