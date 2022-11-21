from app.pieces.pieces import detect_pieces
from app.chesspiece import Square, CHESS_BOARD
from app.chesspiece import Piece
import app.board.board
from math import sqrt

# função que retorna uma matriz preechida de Squares e objetos Pieces inseridos nas posições reais em que foram detectados
def detect_pieces_in_board(pieces, board):
    
    board_Pieces = board
    nearest = board[0][0]
    # lista que armazenará dois ou mais objetos Piece caso estejam em mesma posição em um índice da matriz board_Pieces
    inSamePos = []
    for e in range(len(pieces)):
        # cálculo do ponto médio de Piece
        avPointP = ((pieces(e).bottom_right[0] + pieces(e).top_left[0])/2, (pieces(e).bottom_right[1] + pieces(e).top_left[1])/2)
        for i in board:
            for y in i:
            # cálculo do ponto médio de Square e da posição do tabuleiro mais próxima à Piece
                avPointS = ((y.bottom_right[0] + y.top_left[0])/2, (y.bottom_right[1] + y.top_left[1])/2)
                avPointN = ((nearest.bottom_right[0] + nearest.top_left[0])/2, (nearest.bottom_right[1] + nearest.top_left[1])/2)
            # distância entre dois pontos utilizada para verificar qual a posição do tabuleiro mais próxima à Piece
                if sqrt( pow(avPointP[0] - avPointS[0], 2) + pow(avPointP[1]-avPointS[1], 2)) < sqrt( pow(avPointP[0] - avPointN[0], 2) + pow(avPointP[1]-avPointN[1], 2)):
                    nearest = y
                    indLine = board.index(i)

        # a peça é inserida na matriz board_Pieces em que seu ponto médio mais se aproxima do ponto médio da posição
        if type(board_Pieces[indLine][board.index(nearest)]) != type(pieces[e]):
            board_Pieces[indLine][board.index(nearest)] = pieces[e]

        # se já havia um ou mais objeto(s) Piece inserido(s) a lista inSamePos armazenará estes no índice da posição em board_Pieces
        else:
            aux1 = pieces[e]
            aux2 = board_Pieces[indLine][board.index(nearest)]
            if type(aux2) is list:
                inSamePos.append(aux1)
                for i in aux2:
                    inSamePos.append(i)
                board_Pieces[indLine][board.index(nearest)] = inSamePos
            else:
                board_Pieces[indLine][board.index(nearest)] = inSamePos[aux1, aux2]   
    return board_Pieces
