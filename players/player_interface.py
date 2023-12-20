from ..othello.othello_board import OthelloBoard


class OthelloPlayer:
    def __init__(self, player_id):
        self.player_id = player_id

    def make_move(self, board: OthelloBoard):
        raise NotImplementedError("make_move method must be implemented.")
