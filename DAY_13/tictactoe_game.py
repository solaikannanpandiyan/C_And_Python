class TicTacToe:
    def __init__(self, boardsize):
        self.boardsize = boardsize
        self.board = [[' ' for _ in range(self.boardsize)] for _ in range(self.boardsize)]
        self.current_player = 'X'
    
    def print_board(self):
        print("  0   1   2")
        print("  ---------")
        for i, row in enumerate(self.board):
            print(i, " | ".join(row))
            print("  ---------")
    
    def check_winner(self):
        pass
    
    def make_move(self, row, col):
        pass
    
    def play(self):
        pass


if __name__ == "__main__":
    game = TicTacToe(3)
    game.print_board()
    # game.play()
