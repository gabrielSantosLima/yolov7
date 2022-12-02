from app.utils import get_coordinate
from app.chesspiece import ChessObject, Piece, Square, CHESS_BOARD, COORDINATE
from app.pieces.pieces import detect_pieces
from app.positions.positions import detect_positions, get_positions_of
from app.moves.moves import draw_positions
from app.board.board import detect_board, split_board
from app.positions.piecePosition import detect_pieces_in_board

class Chess:
    def __init__(self, model, minimap):
        self.model = model
        self.minimap = minimap
        self.board: list[list[ChessObject]] = []
        self.isMinimapVisible = False

    def toggle_minimap(self):
        self.isMinimapVisible = not self.isMinimapVisible
        if self.isMinimapVisible:
            self.minimap.show()
        else:
            self.minimap.hide()

    def __find_piece_in_board(self, board: CHESS_BOARD, piece_coordinate: COORDINATE) -> ChessObject:
        x,y = piece_coordinate
        return board[y][x]

    def __is_board_valid(self, board: CHESS_BOARD) -> bool:
        if len(board) != 8: return False
        for row in board:
            if len(row) != 8: return False
        return True

    def run(self, image, crop_coordinates, piece_coordinate: COORDINATE):
        # # Detectando as peças
        pieces: list[Piece] = detect_pieces(image, self.model)

        if len(pieces) == 0: return image

        # Detectando o tabuleiro
        if len(self.board) == 0:
            detected_board = split_board(image, crop_coordinates)
            if not self.__is_board_valid(detected_board): return image
            self.board: list[list[Square]] = detected_board

        # Detectando peças no tabuleiro
        board_with_pieces: CHESS_BOARD = detect_pieces_in_board(pieces, self.board)

        # Buscando a peça desejada no tabuleiro
        piece = self.__find_piece_in_board(board_with_pieces, piece_coordinate)

        # Detectando posições de uma peça, caso ela exista no tabuleiro.
        if isinstance(piece, Piece):
            x,y = piece_coordinate
            
            # positions: list[ChessObject] = detect_positions(board_with_pieces, piece, (x,y))
            positions: list[COORDINATE] = get_positions_of(board_with_pieces, piece, (x,y))

            # Mostrando as posições no minimapa
            if len(positions) > 0:
                self.minimap.paint_squares(coordinates)
            else:
                self.minimap.clear()
            # Desenhando as posições na imagem
            # return draw_positions(image, positions)
            return image