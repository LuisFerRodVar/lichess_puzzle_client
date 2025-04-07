from ui import *
from chess_logic import *
from lichess_api import get_puzzle
import re


def main():
    logic = Logic()
    ui = Ui(logic)
    while True:
        puzzle = get_puzzle()
        logic.load_puzzle(puzzle[0])
        solution = puzzle[1]
        current_player = logic.get_current_player()
        if not (current_player[0] == current_player[1]):
            logic.flip_board()

        while True:
            ui.update_sidebar(current_player[0])
            ui.update_board(logic.parse_board())
            ui.read_moves()
            while True:
                pass


main()
