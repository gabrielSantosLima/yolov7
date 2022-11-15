from app.chesspiece import (CHESS_BOARD, COORDINATE, ChessObject, Piece,ChessPieceEnum, ColorEnum)
from app.positions.positionbuilder import PositionBuilder
from app.utils import get_chess_board_size

def get_positions_of(chess_board: CHESS_BOARD, chess_piece: Piece) -> list[COORDINATE]:
    x,y = chess_piece.board_coordinate
    chess_board_size = get_chess_board_size()
    position_builder = PositionBuilder((x,y), chess_board_size, chess_board)
    
    match get_classname_of(chess_piece.name):
        case ChessPieceEnum.PAWN:
            if get_color_of(chess_piece.name) == ColorEnum.WHITE:
                position_builder.up()
                if y == 6: position_builder.up(2)
            else:
                position_builder.down()
                if y == 1: position_builder.down(2)
        case ChessPieceEnum.KNIGHT: 
            position_builder\
                .up_left(2, 1)\
                .up_left(1, 2)\
                .up_right(2, 1)\
                .up_right(1, 2)\
                .down_left(2, 1)\
                .down_left(1, 2)\
                .down_right(2, 1)\
                .down_right(1, 2)
        case ChessPieceEnum.BISHOP: 
            position_builder\
                .in_primary_diagonal()\
                .in_secondary_diagonal()
        case ChessPieceEnum.ROOK: 
            position_builder\
                .in_column()\
                .in_row()
        case ChessPieceEnum.QUEEN: 
            position_builder\
                .in_column()\
                .in_row()\
                .in_primary_diagonal()\
                .in_secondary_diagonal()
        case ChessPieceEnum.KING: 
            position_builder\
                .up()\
                .up_left()\
                .up_right()\
                .left()\
                .right()\
                .down()\
                .down_left()\
                .down_right()
    
    return position_builder.build()

def find_pieces(chess_board: CHESS_BOARD, color:ColorEnum=None) -> list[Piece]:
    pieces = []
    for row in chess_board:
        for chess_object in row:
            if isinstance(chess_object, Piece):
                if color != None and chess_object.color == color:
                    pieces.append(chess_object)
                elif color == None:
                    pieces.append(chess_object)
    return pieces

def get_color_of(name: str)-> ColorEnum:
    return ColorEnum.WHITE if name.find('white') != -1 else ColorEnum.BLACK

def get_classname_of(name: str) -> ChessPieceEnum:
    for piece in ChessPieceEnum:
        if name.find(piece.value) != -1: 
            return piece
    return ChessPieceEnum.PAWN

def detect_positions(chess_board: CHESS_BOARD, chess_piece: Piece) -> list[ChessObject]:
    positions = get_positions_of(chess_board, chess_piece)
    
    if get_classname_of(chess_piece.name) == ChessPieceEnum.KING:
        enemy_color = ColorEnum.BLACK if get_color_of(chess_piece.name) == ColorEnum.WHITE else ColorEnum.WHITE
        all_positions_of_enemy = []
        for enemy in find_pieces(chess_board, enemy_color):
            all_positions_of_enemy += get_positions_of(chess_board, enemy)
        positions = list(
            filter(lambda position: position not in all_positions_of_enemy, positions)
        )
    
    positions_2_chess_object: list[ChessObject] = list(
        map(lambda x,y: chess_board[y][x], positions)
    )

    return positions_2_chess_object