from enum import Enum


class ChessPieceEnum(Enum):
    PAWN = 'pawn'
    KNIGHT = 'knight'
    BISHOP = 'bishop'
    ROOK = 'rook'
    QUEEN = 'queen'
    KING = 'king'

class ColorEnum(Enum):
    BLACK = 0
    WHITE = 1

COORDINATE = tuple[int, int]

class ChessObject:
    def __init__(
        self, 
        top_left: COORDINATE, 
        top_right: COORDINATE, 
        bottom_right: COORDINATE, 
        bottom_left: COORDINATE
    ):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_right = bottom_right
        self.bottom_left = bottom_left

class Square(ChessObject):
    def __init__(
        self,
        top_left: COORDINATE, 
        top_right: COORDINATE, 
        bottom_right: COORDINATE, 
        bottom_left: COORDINATE
    ):
        super().__init__(top_left, top_right, bottom_right, bottom_left)

class Piece(ChessObject):
    def __init__(
        self, 
        top_left: COORDINATE, 
        top_right: COORDINATE, 
        bottom_right: COORDINATE, 
        bottom_left: COORDINATE,
        name: str,
    ):
        super().__init__(top_left, top_right, bottom_right, bottom_left)
        self.name: str = name
        self.coordinate: COORDINATE = (0,0)

CHESS_BOARD = list[list[ChessObject]]
