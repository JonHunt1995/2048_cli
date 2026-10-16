from game import *

def main():
    game = Game()
    game.board = [0 for _ in range(BOARD_SIZE)]
    game.board[5] = 2

    print_board(game)
    while True:
        command = input('play turn (w=up, s=down, a=left, d=right): ')

        if command not in list('wasd'):
            print('command not acceptable', command)
            continue

        play_turn(game, command)
        blanks = get_blanks(game)
        if not blanks:
            break
        spawn_num(game, blanks)
        print('\n'*3)
        print_board(game)

    print_board(game)

main()