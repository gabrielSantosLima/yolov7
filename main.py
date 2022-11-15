from app.utils import get_coordinate
from app.chesspiece import ChessObject, Piece, Square, CHESS_BOARD
from app.pieces.pieces import DetectPieces
from app.positions.positions import detect_positions 
from app.moves.moves import draw_positions

class Chess:
    def __init__(self, model):
        self.model = model

    def __find_piece_in_board(self, board: CHESS_BOARD, piece_notation: str) -> ChessObject:
        x,y = get_coordinate(piece_notation)
        return board[y][x]

    def __update_coordinates(self, board: CHESS_BOARD):
        for y, row in enumerate(board):
            for x, piece in enumerate(row):
                if isinstance(piece, Piece):
                    piece.coordinate = (x,y)

    def run(self, image):
        # piece_notation = input("Digite a peça que você deseja detectar: ")

        # Detectando as peças
        dp = DetectPieces(self.model)
        pieces: list[Piece] = dp.detect_pieces(image)

        # Detectando o tabuleiro
        board: list[list[Square]] = detect_board(image)

        # Detectando peças no tabuleiro
        board: CHESS_BOARD = detect_pieces_in_board(pieces, board)

        # Atualizando coordenadas das peças
        self.__update_coordinates(board)

        # Buscando a peça desejada no tabuleiro
        piece = self.__find_piece_in_board(board, "e4")

        # Detectando posições de uma peça, caso ela exista no tabuleiro.
        if isinstance(piece, Piece):
            positions: list[ChessObject] = detect_positions(board, piece)

            # Desenhando as posições na imagem
            draw_positions(image, positions)


# if __name__ == '__main__':
#     model = yolov7_model('./best.pt',conf_thres = 0.20,iou_thres = 0.40)
#     main = DetectPieces(model)
#     c = Cameo()
#     c.run(main)