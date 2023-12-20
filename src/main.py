import numpy as np
from utils import *

# start of game logic
# create boards
board_1 = create_board()
board_2 = create_board()
player_stop_request = False
previous_cpu_tries = set()
# welcome player
print('\n🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊')
print('\n🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊')
print('\n🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊')
print('\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢')
print('\n                  Welcome to Battleship!')
print('\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢')
print('\n🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊')
print('\n🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊')
print('\n🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊\n')
print("""Battleship is a strategy game where you play against the
machine. Both of you will have a 10 by 10 board where a 
set of ships will be placed at random. 
      
    > 4 submarines of length 1
    > 3 destroyers of length 2
    > 2 cruisers of length 3
    > 1 battleship of length 4

In the boards, columns are identified by letters, A to J, 
rows are identified by numbers, 1 to 10.
      
You will have to input a guess of both column and row, 
e.g., A1, E10, etc.

These icons will guide you along the way:
     
🌊 Empty or un-navigated sea
🚢 A standing ship (or part of one)
💥 A struck ship (or part of one)
✅ A previously struck position
      
First, you'll have the option to pick a difficulty level.
""")
difficulty_chosen = False
while difficulty_chosen == False:
    try:
        difficulty_input = input('Pick a difficulty level, E for Easy, H for Hard: ')
        match difficulty_input:
            case 'e'  | 'E':
                difficulty = False
                difficulty_chosen = True
                print('Easy Difficulty')
            case 'h' | 'H':
                difficulty = True
                difficulty_chosen = True
                print('Hard Difficulty')
    except:
        print('You must choose a difficulty level')
        continue

print("\nLet's start! Good luck!")
print('\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢')
print('🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊')
# loop while number of cpu boats sunk is below 10
while sunk_check(board_2, 'Your boat #', False) < 10:
    player_has_token = True
    if player_stop_request:
        break
    while player_has_token:
        print("\n--- It's your turn ---")
        # print player's board
        print('\nYour board:\n')
        print(player_board(board_2))
        # print cpu's board
        print('\nCPU\'s board:\n')
        print(opponent_board(board_1))
        print('\n')
        # coordinates input
        print('Input coordinates:')
        try:
            # row, column in a single input
            full_input = input('Column (A to J) and Row (1 to 10) (e.g., A7, J10) (Enter STOP to exit the game): ')
            # stop option for player
            if full_input.lower() == 'stop':
                player_stop_request = True
                print('Bye!')
                break
            column_input = full_input[0]
            row_input = int(full_input[1:])
            # row, column in two separate inputs
            #column_input = input('Column (A to J): ')
            #row_input = int(input('Row (1 to 10): '))
            row, column = input_conversion(row_input, column_input)
        except:
            print('You must input a column letter between A and J and a row number between 1 and 10. Try again.')
            continue
        print('\n')
        # match-case for checking result at coordinates
        match board_1[row, column]:
            case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
                print("YOU'VE HIT CPU!")
                board_1[row, column] = - board_1[row, column]
                if sunk_check(board_1, 'CPU\'s boat #', False) == 10:
                    break
            case -1 | -2 | -3 | -4 | -5 | -6 | -7 | -8 | -9 | -10 | 99:
                print('You already hit that position')
                player_has_token = False
            case 0:
                print('You\'ve hit water')
                board_1[row, column] = 99
                player_has_token = False
    # start of cpu's turn
    if sunk_check(board_1, 'CPU\'s boat #', False) < 10:
        if player_stop_request:
            break
        cpu_has_token = True
        while cpu_has_token:
            cpu_try = np.random.randint(10, size=2)
            if difficulty:
                if (cpu_try[0], cpu_try[1]) in previous_cpu_tries:
                    continue
            previous_cpu_tries.add((cpu_try[0], cpu_try[1]))
            cpu_row = cpu_try[0]
            cpu_column = cpu_try[1]
            # start of logic for cpu's try, while number of player's sunk boats below 10
            print("\n--- It's CPU's turn ---\n")
            match board_2[cpu_row, cpu_column]:
                case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
                    print('CPU\'S HIT YOU!')
                    board_2[cpu_row, cpu_column] = - board_2[cpu_row, cpu_column]
                    if sunk_check(board_2, 'Your boat #', False) == 10:
                        break
                case 0 | -1 | -2 | -3 | -4 | -5 | -6 | -7 | -8 | -9 | -10:
                    print('CPU\'s hit water')
                    cpu_has_token = False
    else:
        print('\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
        print('YOU WON! YOU WON! YOU WON! YOU WON!\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
        # print player's board
        print('\nYour board:\n')
        print(player_board(board_2))
        # print cpu's board
        print('\nCPU\'s board:\n')
        print(opponent_board(board_1))
        print('\n')
        print('\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
        print('YOU WON! YOU WON! YOU WON! YOU WON!\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
        break
else:
    print('\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
    print('CPU WON! CPU WON! CPU WON! CPU WON!\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
    # print player's board
    print('\nYour board:\n')
    print(player_board(board_2))
    # print cpu's board
    print('\nCPU\'s board:\n')
    print(opponent_board(board_1))
    print('\n')
    print('\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
    print('CPU WON! CPU WON! CPU WON! CPU WON!\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢🚢\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
    