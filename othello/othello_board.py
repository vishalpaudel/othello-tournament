import numpy as np

class OthelloBoard:
    WHITE = 'W'
    BLACK = 'B'
    EMPTY = '.'

    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def __init__(self):
        # Initialize an 8x8 board with starting pieces
        self.board = np.full((8, 8), self.EMPTY, dtype=str)
        self.board[3:5, 3:5] = [[self.WHITE, self.BLACK], [self.BLACK, self.WHITE]]

    def get_board(self):
        return self.board

    def make_move(self, move, player_color):
        # Make a move on the board, updating pieces and flipping opponent pieces
        row, col = move

        if self.is_valid_move(row, col, player_color):
            self.board[row, col] = player_color
            self.flip_pieces(row, col, player_color)
            return True
        else:
            return False

    def is_valid_move(self, row, col, player_color):
        # Check if the move is valid
        if self.board[row, col] != self.EMPTY:
            return False

        for dr, dc in self.DIRECTIONS:
            r, c = row + dr, col + dc

            if 0 <= r < 8 and 0 <= c < 8 and self.board[r, c] != self.EMPTY and self.board[r, c] != player_color:
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r, c] == player_color:
                        return True
                    elif self.board[r, c] == self.EMPTY:
                        break
                    r += dr
                    c += dc
        return False



    def flip_pieces(self, row, col, player_color):
        # Implement logic to flip opponent pieces when a move is made
        for dr, dc in self.DIRECTIONS:
            flipped_pieces = []
            r, c = row + dr, col + dc

            while 0 <= r < 8 and 0 <= c < 8 and self.board[r, c] != self.EMPTY and self.board[r, c] != player_color:
                flipped_pieces.append((r, c))
                r += dr
                c += dc

            if 0 <= r < 8 and 0 <= c < 8 and self.board[r, c] == player_color:
                for fr, fc in flipped_pieces:
                    self.board[fr, fc] = player_color

    def display_board(self):
        # Display the current state of the board
        print(self.get_board())

if __name__ == "__main__":
    import copy

    test_board = OthelloBoard()
    # test_board.display_board()

    test_board_array = test_board.get_board()
    for r in range(0, 8):
        for c in range(0, 8):
            copy_board = copy.deepcopy(test_board)
            copy_board.make_move((r, c), 'W')

            copy_board_array = copy_board.get_board()

            if not np.array_equal(test_board_array, copy_board_array):
                print((r, c))
                copy_board.display_board()
