from ui import *
from chess_logic import *


def main():
    logic = Logic()
    ui = Ui()
    ui.update_board(logic.parse_board())


main()
