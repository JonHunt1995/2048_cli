import random
import itertools
from dataclasses import dataclass, field
from collections.abc import Callable

BOARD_LENGTH, BOARD_WIDTH = 4, 4
BOARD_SIZE = BOARD_LENGTH * BOARD_WIDTH

@dataclass
class Game:
    score: int = 0                  
    highest: int = 2         
    board: list[int] = field(default_factory=list)

def print_board(game: Game):
    for i in range(BOARD_LENGTH):
        offset = i*BOARD_WIDTH
        row = game.board[offset:offset+BOARD_WIDTH]
        print('\t'.join(str(x).rjust(4) for x in row))
        print()

    print(f"score: {game.score} highest: {game.highest}")

def get_blanks(game: Game):
    return [i for i, num in enumerate(game.board) if num == 0]
    
def spawn_num(game: Game, blanks: list[int]):
    next_spawn = random.choice(blanks)
    game.board[next_spawn] = 2 if random.randint(0, 100) <= 90 else 4

def shift_row_or_col(game: Game, indices: list[int], fn: Callable[[list[int]], int]):
    if not [i for i, num in enumerate(indices) if game.board[num] == 0]:
        return

    for idx in indices:
        num = game.board[idx]

        if num == 0:
            continue
        zero_indices = (i for i in indices if game.board[i] == 0)
        zero_to_swap = fn(zero_indices)
        if fn(idx, zero_to_swap) == idx:
            continue

        game.board[idx], game.board[zero_to_swap] = game.board[zero_to_swap], game.board[idx]

def merge_duplicates(game: Game, indices: list[int]):
    for first, sec in itertools.pairwise(indices):
        if game.board[first] == game.board[sec]:
            new_square = game.board[first] + game.board[sec]
            game.score += new_square
            game.highest = max(game.highest, new_square)
            game.board[first], game.board[sec] = new_square, 0

    
def shift_board(game: Game, vert=True, asc=True):
    fn = max if not asc else min
    for i in range(BOARD_WIDTH):
        if not vert:
            indices = [x for x in range(i*BOARD_LENGTH, i*BOARD_LENGTH + BOARD_WIDTH)]
        else:
            indices = [x for x in range(i, BOARD_SIZE, 4)]
        if not asc:
            indices = indices[::-1]

        shift_row_or_col(game, indices, fn)
        merge_duplicates(game, indices)
        shift_row_or_col(game, indices, fn)

def play_turn(game: Game, command: str):
    match command:
        case 'w':
            shift_board(game, vert=True, asc=True)
        case 's':
            shift_board(game, vert=True, asc=False)
        case 'a':
            shift_board(game, vert=False, asc=True)
        case 'd':
            shift_board(game, vert=False, asc=False)
        