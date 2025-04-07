import tkinter as tk
from config import *
from chess_logic import Logic
import re


class Ui:
    def __init__(self, logic):
        self.root = tk.Tk()
        self.root.title("Lichess Puzzle")
        self.root.geometry("1024x600")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.bind("<Key>", self.key_press)
        self.seconds = 0
        self.running = False
        self.timer_id = None
        self.logic = logic

        self.create_sidebar()
        self.create_board()

    def key_press(self, event):
        current_key = event.char
        self.current_input += current_key
        print(self.current_input)
        if not(any(subc.startswith(self.current_input) for subc in self.movelist)):
            self.current_input = ""
        else:
            if self.current_input in self.movelist:
                for i in range(len(self.movelist)-1):
                    # FIX: The move input is not working
                    if (self.current_input == self.movelist[i]):
                        self.logic.push_move(self.movelist_aux[i])
                        break

        self.update()

    def start_inputs(self):
        legal_moves = str(self.logic.get_legal_moves())
        legal_movesl = legal_moves.lower()
        regular_expresion = re.search(r'\((.*?)\)', legal_movesl)
        regular_expresion2 = re.search(r'\((.*?)\)', legal_moves)
        self.movelist = regular_expresion.group(1).split(", ")
        self.movelist_aux = regular_expresion2.group(1).split(", ")
        self.current_input = ""

    def read_moves(self):
        self.start_inputs()
        self.update()



    def create_sidebar(self):
        self.sidebar = tk.Frame(self.root, width=400, bg=BACKGROUND_COLOR, padx=10, pady=10)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.info_label = tk.Label(self.sidebar, text="⏺ Tu turno ⏺", fg="white", bg="#2E3440", font=("Arial", 48, "bold"))
        self.info_label.pack(pady=10)
        self.time_label = tk.Label(self.sidebar, text="Tiempo: 00:00", fg="white", bg="#2E3440", font=("Arial", 28))
        self.time_label.pack(side="bottom", pady=5)

    def update_sidebar(self, isWhite):
        bcolor = BACKGROUND_COLOR if isWhite else BACKGROUND_COLOR2
        fcolor = TEXT_COLOR if isWhite else TEXT_COLOR2
        self.info_label.config(bg=bcolor, fg=fcolor)

    def create_board(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.grid(row=0, column=1, sticky="nsew")

        self.board = []
        for row in range(8):
            rowData = []
            self.board_frame.grid_rowconfigure(row, weight=1, minsize=50)
            for col in range(8):
                color = LIGHT_SQUARES if (row + col) % 2 == 0 else DARK_SQUARES
                button = tk.Button(self.board_frame, width=5, height=5, bg=color, relief="flat", highlightthickness=0, font=("Arial", 42))
                button.grid(row=row, column=col, sticky="nsew")
                rowData.append(button)
            self.board.append(rowData)

        for col in range(8):
            self.board_frame.grid_columnconfigure(col, weight=1, minsize=50)

    def update_board(self, position):
        pieces = {"p": "♟", "k": "♚", "q": "♛", "r": "♜", "b": "♝", "n": "♞", ".": " "}
        for row in range(8):
            currentRow = position[row]
            for col in range(8):
                square = currentRow[col]
                color = WHITE_PIECES if square[0].isupper() else BLACK_PIECES
                piece = pieces[square.lower()]
                self.board[row][col].config(fg=color, text=piece)

    def update(self):
        self.root.mainloop()

    def update_timer(self):
        if self.running:
            self.seconds += 1
            mins, secs = divmod(self.seconds, 60)
            self.time_label.config(text=f"Tiempo: {mins:02}:{secs:02}")
            self.timer_id = self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def reset_timer(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        self.seconds = 0
        self.time_label.config(text="Tiempo: 00:00")
        self.running = False
        self.start_timer()
