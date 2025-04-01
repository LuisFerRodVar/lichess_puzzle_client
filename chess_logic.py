import chess


class Logic:
    def __init__(self):
        self.board = chess.Board()

    def push_move(self, move):
        self.board.push(move)

    def get_board(self):
        return str(self.board)

    def parse_board(self):
        board = str(self.board).split("\n")
        result = []
        for current in board:
            result += [current.split(" ")]
        return result
