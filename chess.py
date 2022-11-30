from app.utils import get_coordinate
from app.chesspiece import ChessObject, Piece, Square, CHESS_BOARD
from app.pieces.pieces import detect_pieces
from app.positions.positions import detect_positions 
from app.moves.moves import draw_positions
from app.board.board import detect_board
from app.positions.piecePosition import detect_pieces_in_board

class Chess:
    def __init__(self, model):
        self.model = model
        self.board: list[list[ChessObject]] = []
        self.pieces: list[Piece] = []

    def __find_piece_in_board(self, board: CHESS_BOARD, piece_notation: str) -> ChessObject:
        x,y = get_coordinate(piece_notation)
        return board[y][x]

    def __update_coordinates(self, board: CHESS_BOARD):
        for y, row in enumerate(board):
            for x, piece in enumerate(row):
                if isinstance(piece, Piece):
                    piece.coordinate = (x,y)

    def __is_board_valid(self, board: CHESS_BOARD) -> bool:
        if len(board) != 8: return False
        for row in board:
            if len(row) != 8: return False
        return True

    def run(self, image):
        # piece_notation = input("Digite a peça que você deseja detectar: ")

        # # Detectando as peças
        pieces: list[Piece] = detect_pieces(image, self.model)
        if len(pieces) != 0: self.pieces = pieces.copy()

        # Detectando o tabuleiro
        if len(self.board) == 0:
            detected_board = detect_board(image, output='out.png')
            if not self.__is_board_valid(detected_board): return
            self.board: list[list[Square]] = detected_board


        # Detectando peças no tabuleiro
        board_with_pieces: CHESS_BOARD = detect_pieces_in_board(pieces, self.board)

        # Atualizando coordenadas das peças
        self.__update_coordinates(board_with_pieces)

        # Buscando a peça desejada no tabuleiro
        piece = self.__find_piece_in_board(board_with_pieces, "e4")

        # Detectando posições de uma peça, caso ela exista no tabuleiro.
        if isinstance(piece, Piece):
            positions: list[ChessObject] = detect_positions(board_with_pieces, piece)

            # Desenhando as posições na imagem
            return draw_positions(image, positions)