import chess


class Logic:
    def __init__(self):
        self.flipped = True
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

    def load_puzzle(self, pgn):
        self.board = chess.Board()
        if not (self.flipped):
            self.flip_board()
        for move in pgn.split(" "):
            self.board.push_san(move)

    def get_current_player(self):
        if "w" in self.board.fen():
            return (True, self.flipped)
        return (False, self.flipped)

    def flip_board(self):
        self.board = self.board.transform(chess.flip_vertical)
        self.board = self.board.transform(chess.flip_horizontal)
        self.flipped = not (self.flipped)

    def get_legal_moves(self):
        return self.board.legal_moves
