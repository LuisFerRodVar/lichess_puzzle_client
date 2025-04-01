import tkinter as tk
from config import *


class Ui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lichess Puzzle")
        self.root.geometry("1024x600")  # Ajuste del tamaño para una mejor distribución
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=0)  # Panel izquierdo con tamaño fijo
        self.root.grid_columnconfigure(1, weight=1)  # Tablero adaptable

        self.create_sidebar()
        self.create_board()

    def create_sidebar(self):
        self.sidebar = tk.Frame(self.root, width=400, bg="#2E3440", padx=10, pady=10)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        
        self.info_label = tk.Label(self.sidebar, text="Información de la partida lalalalalalallalaala ", fg="white", bg="#2E3440", font=("Arial", 14, "bold"))
        self.info_label.pack(pady=10)
        
        self.move_label = tk.Label(self.sidebar, text="Movimientos: 0", fg="white", bg="#2E3440", font=("Arial", 12))
        self.move_label.pack(pady=5)
        
        self.time_label = tk.Label(self.sidebar, text="Tiempo: 00:00", fg="white", bg="#2E3440", font=("Arial", 12))
        self.time_label.pack(pady=5)

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
        pieces = {
            "p": "♟", "k": "♚", "q": "♛", "r": "♜", "b": "♝", "n": "♞", ".": " "
        }
        for row in range(8):
            currentRow = position[row]
            for col in range(8):
                square = currentRow[col]
                color = WHITE_PIECES if (square[0].isupper()) else BLACK_PIECES
                piece = pieces[square.lower()]
                self.board[row][col].config(fg=color, text=piece)
        self.update()

    def update(self):
        self.root.mainloop()

