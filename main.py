from ui import *
from chess_logic import *


def main():
    logic = Logic()
    ui = Ui()
    ui.update()
    print(logic.parse_board())


main()
