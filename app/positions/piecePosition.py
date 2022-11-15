from app.pieces.detectPieces import DetectPieces
from chesspiece import Square, CHESS_BOARD


# lista que armazena as peças detectadas
listPieces = DetectPieces.detect_pieces

# variável ilustrativa, a qual representa uma matriz preenchida por instâncias de Square, ou seja, um tabuleiro.
# Deve-se posteriormente substituir esta pela matriz real que armazena instâncias de Square cuja base são imagens de tabuleiro.
board: CHESS_BOARD = []
for row in range(8):
    board.append([])
    for column in range(8):
        board[row].append(
            Square(row * 10, column * 10, 10, 10, (column, row))
        )

# o algoritmo considera que os dois primeiros atributos de Square são coordenadas centrais ao quadrado
def detect_pieces_in_board(pieces, board):
    
    nearer = board[0]
    piece_and_pos = []
    for e in range(len(pieces)):
        for i in board:
             if (abs(nearer.x - (pieces[e].y + pieces[e].y2)/2)) > (abs(board[i].x - (pieces[e].y + pieces[e].y2)/2)):
                nearer = board[e]
        piece_and_pos.append((pieces[e], nearer))
    return piece_and_pos
