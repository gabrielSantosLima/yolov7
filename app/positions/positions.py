from chesspiece import (CHESS_BOARD, COORDINATE, ChessObject, ChessPiece,
                        ChessPieceEnum, ColorEnum, Square)
from positionbuilder import PositionBuilder
from utils import get_chess_board_size, get_coordinate, get_notation


def get_positions_of(chess_board: CHESS_BOARD, chess_piece: ChessPiece) -> list[COORDINATE]:
    x,y = chess_piece.board_coordinate
    chess_board_size = get_chess_board_size()
    position_builder = PositionBuilder((x,y), chess_board_size, chess_board)
    
    match chess_piece.type:
        case ChessPieceEnum.PAWN:
            if chess_piece.color == ColorEnum.WHITE:
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

def get_allowed_positions_of(chess_board: CHESS_BOARD, chess_piece: ChessPiece) -> list[COORDINATE]:
    positions = get_positions_of(chess_board, chess_piece)
    
    if chess_piece.type == ChessPieceEnum.KING:
        enemy_color = ColorEnum.BLACK if chess_piece.color == ColorEnum.WHITE else ColorEnum.WHITE
        all_positions_of_enemy = []
        for enemy in find_pieces(chess_board, enemy_color):
            all_positions_of_enemy += get_positions_of(chess_board, enemy)
        positions = list(
            filter(lambda position: position not in all_positions_of_enemy, positions)
        )
    
    return positions

def find_pieces(chess_board: CHESS_BOARD, color:ColorEnum=None) -> list[ChessPiece]:
    pieces = []
    for row in chess_board:
        for chess_object in row:
            if isinstance(chess_object, ChessPiece):
                if color != None and chess_object.color == color:
                    pieces.append(chess_object)
                elif color == None:
                    pieces.append(chess_object)
    return pieces 

# Temp
def print_board(chess_board: CHESS_BOARD):
    for row in range(8):
        for column in range(8):
            el = chess_board[row][column]
            if isinstance(chess_board[row][column], ChessPiece):
                print(el.type.value, end='')
            print(get_notation(el.board_coordinate[0], el.board_coordinate[1]), end=' ')
        print()

if __name__ == '__main__':
    board: CHESS_BOARD = []
    
    for row in range(8):
        board.append([])
        for column in range(8):
            board[row].append(
                Square(row * 10, column * 10, 10, 10, (column, row))
            )
    
    board[0][0] = ChessPiece(
        ChessPieceEnum.ROOK, 
        ColorEnum.BLACK, 
        10, 
        10, 
        10, 
        10, 
        get_coordinate('a8')
    )
    board[4][3] = ChessPiece(
        ChessPieceEnum.ROOK, 
        ColorEnum.WHITE, 
        10, 
        10, 
        10, 
        10, 
        get_coordinate('d4')
    )
    board[0][3] = ChessPiece(
        ChessPieceEnum.QUEEN, 
        ColorEnum.BLACK, 
        10, 
        10, 
        10, 
        10, 
        get_coordinate('d8')
    )
    board[5][3] = ChessPiece(
        ChessPieceEnum.KING, 
        ColorEnum.WHITE,
        30,
        30,
        10,
        10,
        get_coordinate('d3')
    )
    
    positions = get_allowed_positions_of(board, board[5][3])
    positions_notations = list(
        map(lambda coordinate: get_notation(coordinate[0], coordinate[1]), positions)
    )
    print_board(board)
    print(positions)
    print(positions_notations)
