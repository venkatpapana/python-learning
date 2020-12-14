from random import randrange

board_size = 3


def display_board(board):
    for row in board:
        print('+-----+-----+-----+')
        for col in row:
            print('|  ' + str(col), end='  ')
        print('|')
    print('+-----+-----+-----+')


def get_row_col_from_choice(choice):
    choice -= 1
    row, col = choice // 3, choice % 3
    return row, col


def user_turn():
    while True:
        pos = input('Enter your choice(1-9): ')
        if pos == '':
            confirm = input('Are you sure to Exit (y/n)?')
            if confirm == 'y' or confirm == 'Y':
                return None
            else:
                continue
        pos = int(pos)
        if pos < 1 or pos > 9:
            print('Choose between 1-9')
            continue

        if pos in filled:
            print('Can not overwrite')
            continue
        filled.append(pos)
        filled.sort()

        row, col = get_row_col_from_choice(pos)
        board[row][col] = user_sign
        return True

def prog_turn(board):
    choice = randrange(board_size ** 2)
    choice += 1
    if choice in filled:
        prog_turn(board)
    else:
        print( 'My choice:', choice)
        filled.append(choice)
        filled.sort()
        row, col = get_row_col_from_choice(choice)
        board[row][col] = prog_sign



def is_won(board, sign):
    global board_size
    # rows
    for row in board:
        count = 0
        for col in row:
            if col == sign:
                count += 1

        if count == 3:
            return True

    # cols
    for col in range(board_size):
        count = 0
        for row in range(board_size):
            if board[row][col] == sign:
                count += 1

        if count == 3:
            return True

    # diagnal-1
    count = 0
    col = 0
    for row in range(board_size):
        if board[row][col] == sign:
            count += 1
        col += 1

    if count == 3:
        return True

    # diagnal-2
    count = 0
    col = 2
    for row in range(board_size):
        if board[row][col] == sign:
            count += 1
        col -= 1

    if count == 3:
        return True


prog_sign = 'X'
user_sign = 'O'
board = [
    ['1', '2', '3'],
    ['4', prog_sign, '6'],
    ['7', '8', '9']
]


filled = [5]
display_board(board)
prog_won, user_won = False, False

while len(filled) < 9:
    ret = user_turn()
    if ret is None:
        break

    if is_won(board, user_sign):
        user_won = True
        display_board(board)
        print('You Won!')
        break
    if len(filled) < 9:
        prog_turn(board)
    display_board(board)
    if is_won(board, prog_sign):
        prog_won = True
        print('I Won!')
        break

if len(filled) == 9 and user_won == False and prog_won == False:
    print('Draw!')

