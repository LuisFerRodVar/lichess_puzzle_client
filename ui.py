import tkinter as tk
from config import *


class Ui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lichess Puzzle")
        self.root.geometry("600x600")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.board = []
        self.create_board()

    def update(self):
        self.root.mainloop()

    def create_board(self):
        for row in range(8):
            rowData = []
            self.root.grid_rowconfigure(row, weight=1, minsize=50)
            for col in range(8):
                color = LIGHT_SQUARES if (row + col) % 2 == 0 else DARK_SQUARES
                button = tk.Button(self.root, width=5, height=5, bg=color, relief="flat", highlightthickness=0, font=("Arial", 42))
                button.grid(row=row, column=col, sticky="nsew")
                rowData.append(button)
            self.board.append(rowData)
        for col in range(8):
            self.root.grid_columnconfigure(col, weight=1, minsize=50)

    def update_board(self, position):
        pieces = {
            "p": "♟",
            "k": "♚",
            "q": "♛",
            "r": "♜",
            "b": "♝",
            "n": "♞",
            ".": " "
        }
        for row in range(8):
            currentRow = position[row]
            for col in range(8):
                square = currentRow[col]
                color = WHITE_PIECES if (square[0].isupper()) else BLACK_PIECES
                piece = pieces[square.lower()]
                self.board[row][col].config(
                    fg=color, text=piece)
        self.update()

