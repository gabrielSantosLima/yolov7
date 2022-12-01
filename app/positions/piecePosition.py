from app.pieces.pieces import detect_pieces
from app.chesspiece import Square, CHESS_BOARD
from app.chesspiece import Piece
from app.chesspiece import COORDINATE
import app.board.board
from math import sqrt

def __copy__(board: list[list[Square]]) -> list[list[Square]]:
    copy: list[list[Square]] = []
    for index, row in enumerate(board):
        copy.append([])
        for chess_object in row:
            copy[index].append(chess_object)
    return copy
    
# função que retorna uma matriz preechida de Squares e objetos Pieces inseridos nas posições reais em que foram detectados
def detect_pieces_in_board(pieces, board: list[list[Square]]):
    
    board_copy = __copy__(board)
    nearest = board[0][0]
    # lista que armazenará dois ou mais objetos Piece caso estejam em mesma posição em um índice da matriz board_Pieces
    for e in range(len(pieces)):
        coordinate: COORDINATE = (0,0)
        # cálculo do ponto médio de Piece
        avPointP = ((pieces[e].bottom_right[0] + pieces[e].top_left[0])/2, pieces[e].bottom_right[1])
        for row_index, row in enumerate(board):
            for column_index, current_square in enumerate(row):
            # cálculo do ponto médio de Square e da posição do tabuleiro mais próxima à Piece
                avPointS = ((current_square.bottom_right[0] + current_square.top_left[0])/2, (current_square.bottom_right[1] + current_square.top_left[1])/2)
                avPointN = ((nearest.bottom_right[0] + nearest.top_left[0])/2, (nearest.bottom_right[1] + nearest.top_left[1])/2)
            # distância entre dois pontos utilizada para verificar qual a posição do tabuleiro mais próxima à Piece
                if sqrt( pow(avPointP[0] - avPointS[0], 2) + pow(avPointP[1]-avPointS[1], 2)) < sqrt( pow(avPointP[0] - avPointN[0], 2) + pow(avPointP[1]-avPointN[1], 2)):
                    nearest = current_square
                    row_index = board.index(row)
                    coordinate = (row_index, column_index)

        # a peça é inserida na matriz board_Pieces em que seu ponto médio mais se aproxima do ponto médio da posição
        y,x = coordinate
        board_copy[y][x] = pieces[e]

        # se já havia um ou mais objeto(s) Piece inserido(s) a lista inSamePos armazenará estes no índice da posição em board_Pieces
        # else:
        #     aux1 = pieces[e]
        #     aux2 = chess_object
        #     if type(aux2) is list:
        #         is_same_position.append(aux1)
        #         for row in aux2:
        #             is_same_position.append(row)
        #         chess_object = is_same_position
        #     else:
        #         chess_object = is_same_position[aux1, aux2]   
    return board_copy
