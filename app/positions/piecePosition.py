from app.pieces.pieces import detect_pieces
from app.chesspiece import Square, CHESS_BOARD
from app.chesspiece import Piece
import app.board.board
from math import sqrt

# o algoritmo considera que os dois primeiros atributos de Square são coordenadas centrais ao quadrado
def detect_pieces_in_board(pieces, board):
    
    nearest = board[0]
    piece_and_pos = []
    for e in range(len(pieces)):
        for i in board:
            # cálculo do ponto médio de Piece, Square e da posição do tabuleiro mais próxima à Piece
            avPointP = ((pieces(e).bottom_right[0] + pieces(e).top_left[0])/2, (pieces(e).bottom_right[1] + pieces(e).top_left[1])/2)
            avPointS = ((board(i).bottom_right[0] + board(i).top_left[0])/2, (board(i).bottom_right[1] + board(i).top_left[1])/2)
            avPointN = ((nearest.bottom_right[0] + nearest.top_left[0])/2, (nearest.bottom_right[1] + nearest.top_left[1])/2)
            # distância entre dois pontos utilizada para verificar qual a posição do tabuleiro mais próxima à Piece
            if sqrt( pow(avPointP[0] - avPointS[0], 2) + pow(avPointP[1]-avPointS[1], 2)) < sqrt( pow(avPointP[0] - avPointN[0], 2) + pow(avPointP[1]-avPointN[1], 2)):
                nearest = board[i]
        # lista cujos elementos são tuplas com a Piece e sua posição no tabuleiro
        piece_and_pos.append((pieces[e], nearest))
    return piece_and_pos
