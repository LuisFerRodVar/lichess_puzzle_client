from ui import *
from chess_logic import *
from lichess_api import get_puzzle


def main():
    logic = Logic()
    ui = Ui()
    puzzle = get_puzzle()
    logic.load_puzzle(puzzle[0])
    print(puzzle[1])
    if logic.get_current_player()[0]:
        pass
    else:
        logic.flip_board()
    ui.update_sidebar(logic.get_current_player()[0])
    ui.update_board(logic.parse_board())


main()
