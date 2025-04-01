import tkinter as tk


class Ui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lichess Puzzle")
        self.root.geometry("600x600")

    def update(self):
        self.root.mainloop()


