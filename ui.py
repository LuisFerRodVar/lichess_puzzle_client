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

        # Timer
        self.seconds = 0
        self.running = False
        self.timer_id = None  # Guardar la referencia al timer

        self.create_sidebar()
        self.create_board()

    def create_sidebar(self):
        self.sidebar = tk.Frame(self.root, width=400, bg=BACKGROUND_COLOR, padx=10, pady=10)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.info_label = tk.Label(self.sidebar, text="⏺ Tu turno ⏺", fg="white", bg="#2E3440", font=("Arial", 48, "bold"))
        self.info_label.pack(pady=10)

        self.move_label = tk.Label(self.sidebar, text="Movimientos: 0", fg="white", bg="#2E3440", font=("Arial", 12))
        self.move_label.pack(pady=5)

        # Label para el Timer
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
        self.update()

    def update(self):
        self.root.mainloop()

    # -------------------------------
    # ⏳ TIMER METHODS
    # -------------------------------
    def update_timer(self):
        """Actualiza el timer cada segundo."""
        if self.running:
            self.seconds += 1
            mins, secs = divmod(self.seconds, 60)
            self.time_label.config(text=f"Tiempo: {mins:02}:{secs:02}")
            self.timer_id = self.root.after(1000, self.update_timer)

    def start_timer(self):
        """Inicia el timer si no está corriendo."""
        if not self.running:
            self.running = True
            self.update_timer()

    def reset_timer(self):
        """Reinicia el timer a 0, detiene el anterior y lo vuelve a iniciar."""
        # Detener el timer anterior si existe
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        
        self.seconds = 0
        self.time_label.config(text="Tiempo: 00:00")
        self.running = False
        self.start_timer()

