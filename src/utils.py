import numpy as np
import random

# boat placing function

def boat_placer(board, boat_length, boat_number):
    while True:
        # randomly pick a heading for the boat
        heading = random.choice(['N', 'E', 'S', 'W'])

        # boat starting coordinate
        current_pos = np.random.randint(10, size=2)

        row = current_pos[0]
        column = current_pos[1]

        # 4 posible boat headings from starting coordinate
        pos_coord_N = board[row:(row - boat_length):-1, column]
        pos_coord_E = board[row, column:(column + boat_length)]
        pos_coord_S = board[row:(row + boat_length), column]
        pos_coord_W = board[row, column:(column - boat_length):-1]

        # check for validity
        # north heading
        if heading == 'N' and 0 <= (row - boat_length) < 10 and sum(pos_coord_N) == 0:
            board[row:(row - boat_length):-1, column] = boat_number
            break

        # east heading
        elif heading == 'E' and 0 <= (column + boat_length) < 10 and sum(pos_coord_E) == 0:
            board[row, column:(column + boat_length)] = boat_number
            break

        # south heading
        elif heading == 'S' and 0 <= (row + boat_length) < 10 and sum(pos_coord_S) == 0:
            board[row:(row + boat_length), column] = boat_number
            break
        
        # west heading
        elif heading == 'W' and 0 <= (column - boat_length) < 10  and sum(pos_coord_W) == 0:
            board[row, column:(column - boat_length):-1] = boat_number
            break

        # we do not meet the conditions to place the boat in the coordinates and heading defined    
        else:
            continue

# using the boat_placer function, create a full board for the game

def create_board():
    # we start with an empty board
    board = np.zeros((10,10), dtype=np.int32)

    #place boats:
    boat_placer(board, 1, 1)
    boat_placer(board, 1, 2)
    boat_placer(board, 1, 3)
    boat_placer(board, 1, 4)
    boat_placer(board, 2, 5)
    boat_placer(board, 2, 6)
    boat_placer(board, 2, 7)
    boat_placer(board, 3, 8)
    boat_placer(board, 3, 9)
    boat_placer(board, 4, 10)
    return board

# check for ammount of sunk boats
def sunk_check(board, player, expose=True):
    sunk = 0
    for i in range(1,11):
        if i not in board:
            if expose:
                print(player, i, 'has sunk')
            sunk += 1
    return sunk

# creates board to be shown to player of the current situtation of opponent's board
def opponent_board(board):
    
    board_inside = np.full((10,10), '🌊')

    column_indices = [' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J']
    row_indices = np.array([['  '],
                            [' 1'],
                            [' 2'],
                            [' 3'],
                            [' 4'],
                            [' 5'],
                            [' 6'],
                            [' 7'],
                            [' 8'],
                            [' 9'],
                            ['10']])

    board_columns = np.vstack([column_indices, board_inside])
    board_shown = np.hstack([row_indices, board_columns])

    #board_shown = np.full((10,10), '🌊')

    for x in range(10):
        for y in range(10):
            if board[x,y] < 0:
                board_shown[(x + 1),(y + 1)] = '💥'
            elif board[x,y] == 99:
                board_shown[(x + 1),(y + 1)] = '✅'
    return board_shown

# creates board to be shown to player of its own board
def player_board(board):

    board_inside = np.full((10,10), '🌊')

    column_indices = [' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J']
    row_indices = np.array([['  '],
                            [' 1'],
                            [' 2'],
                            [' 3'],
                            [' 4'],
                            [' 5'],
                            [' 6'],
                            [' 7'],
                            [' 8'],
                            [' 9'],
                            ['10']])

    board_columns = np.vstack([column_indices, board_inside])
    board_shown = np.hstack([row_indices, board_columns])


    #board_shown = np.full((10,10), '🌊')

    for x in range(10):
        for y in range(10):
            if board[x,y] < 0:
                board_shown[(x + 1),(y + 1)] = '💥'
            elif board[x,y] > 0:
                board_shown[(x + 1),(y + 1)] = '🚢'
    return board_shown

# converts inputs from rows 1 to 10 and columns A to J to 0-9 matrix indices
def input_conversion(row, column):
    if row > 0 and row < 11:
        row_returned = row - 1
    match column:
        case 'A' | 'a':
            column_returned = 0
        case 'B' | 'b':
            column_returned = 1
        case 'C' | 'c':
            column_returned = 2
        case 'D' | 'd':
            column_returned = 3
        case 'E' | 'e':
            column_returned = 4
        case 'F' | 'f':
            column_returned = 5
        case 'G' | 'g':
            column_returned = 6
        case 'H' | 'h':
            column_returned = 7
        case 'I' | 'i':
            column_returned = 8
        case 'J' | 'j':
            column_returned = 9
    return row_returned, column_returned
