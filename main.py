from ui import *
from chess_logic import *
from lichess_api import get_puzzle
import keyboard
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
            legal_moves = str(logic.get_legal_moves())
            regular_expresion = re.search(r'\((.*?)\)', legal_moves)
            movelist = regular_expresion.group(1).split(", ")
            current_move = ""
            ui.update()
            while True:
                event = keyboard.read_event(suppress=True)
                if event.event_type == keyboard.KEY_DOWN and event.name.isalnum():
                    current_move += event.name
                    if not(any(subc in movelist for subc in current_move)):
                        current_move = ""
                    else:
                        if current_move in movelist:
                            logic.push_move(current_move)
                            break


            




main()
