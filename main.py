from game import *

def main():
    board = [0 for _ in range(BOARD_SIZE)]
    game_over = False
    board[5] = 2

    print_board(board)
    while not game_over:
        command = input('play turn (w=up, s=down, a=left, d=right): ')
        if command not in'wasd':
            print('command not acceptable', command)
            continue
        play_turn(board, command)
        blanks = get_blanks(board)
        if not blanks:
            game_over = True
            break
        spawn_num(board, blanks)
        print('\n'*3)
        print_board(board)

    print_board(board)

main()