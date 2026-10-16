import random
import itertools

BOARD_LENGTH, BOARD_WIDTH = 4, 4
BOARD_SIZE = BOARD_LENGTH * BOARD_WIDTH

def print_board(board):
    for i in range(BOARD_LENGTH):
        offset = i*BOARD_WIDTH
        print(board[offset:offset+BOARD_WIDTH])

def get_blanks(board):
    return [i for i, num in enumerate(board) if num == 0]
    
def spawn_num(board, blanks):
    next_spawn = random.choice(blanks)
    board[next_spawn] = 2

def shift_row_or_col(board, indices, fn):
    if not [i for i, num in enumerate(indices) if board[num] == 0]:
        return

    for idx in indices:
        num = board[idx]

        if num == 0:
            continue
        zero_indices = (i for i in indices if board[i] == 0)
        zero_to_swap = fn(zero_indices)
        if fn(idx, zero_to_swap) == idx:
            continue

        board[idx], board[zero_to_swap] = board[zero_to_swap], board[idx]

def merge_duplicates(board, indices):
    for first, sec in itertools.pairwise(indices):
        if board[first] == board[sec]:
            board[first], board[sec] = board[first] + board[sec], 0

    
def shift_board(board, vert=True, reversed=True):
    fn = max if reversed else min
    for i in range(BOARD_WIDTH):
        if not vert:
            indices = [x for x in range(i*BOARD_LENGTH, i*BOARD_LENGTH + BOARD_WIDTH)]
        else:
            indices = [x for x in range(i, BOARD_SIZE, 4)]
        if reversed:
            indices = indices[::-1]

        shift_row_or_col(board, indices, fn)
        merge_duplicates(board, indices)
        shift_row_or_col(board, indices, fn)

def play_turn(board, command):
    match command:
        case 'w':
            shift_board(board, vert=True, reversed=False)
        case 's':
            shift_board(board, vert=True, reversed=True)
        case 'a':
            shift_board(board, vert=False, reversed=False)
        case 'd':
            shift_board(board, vert=False, reversed=True)