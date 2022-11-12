# Detecção de peças de xadrez utilizando IA e Visão Computacional com Yolov7

## Sumário

- [Passo 1: Lendo a peça desejada](#passo-1-lendo-a-peça-desejada)
- [Passo 2: Detectando as peças em uma imagem](#passo-2-detectando-as-peças-em-uma-imagem)
- [Passo 3: Detectando o tabuleiro](#passo-3-detectando-o-tabuleiro)
- [Passo 4: Detectando as peças no tabuleiro](#passo-4-detectando-as-peças-no-tabuleiro)
- [Passo 5: Detectando posições de uma determinada peça](#passo-5-detectando-posições-de-uma-determinada-peça)
- [Passo 6: Desenhando as posições na imagem](#passo-6-desenhando-as-posições-na-tela)
- [Autores](#autores)

## Passo 1: Lendo a peça desejada

Ler qual peça que o usuário vai querer saber a posição. Abaixo segue as opções possíveis:

| Peça   | Entrada                  | Exemplo |
| ------ | ------------------------ | ------- |
| Peão   | coordenada da casa       | e4      |
| Cavalo | "C" + coordenada da casa | Ce4     |
| Bispo  | "B" + coordenada da casa | Be4     |
| Torre  | "T" + coordenada da casa | Te4     |
| Dama   | "D" + coordenada da casa | De4     |
| Rei    | "R" + coordenada da casa | Re4     |

```python
piece_notation = input("Digite a peça que você deseja detectar: ")
```

## Passo 2: Detectando as peças em uma imagem

Detecta todas as peças em uma imagem

```python
class Piece: # Tem as coordenadas dos 4 cantos do retângulo
    top_left: tuple[int, int] # Recebe como (x,y)
    top_right: tuple[int, int]
    bottom_right: tuple[int, int]
    bottom_left: tuple[int, int]
    name: str
```

```python
# Detectando as peças
pieces: list[Piece] = detect_pieces(image)
```

## Passo 3: Detectando o tabuleiro

Detecta o tabuleiro

```python
class Square: # Tem as coordenadas dos 4 cantos do retângulo
    top_left: tuple[int, int] # Recebe como (x,y)
    top_right: tuple[int, int]
    bottom_right: tuple[int, int]
    bottom_left: tuple[int, int]
```

```python
# Detectando o tabuleiro
board: list[list[Square]] = detect_board(image)
```

## Passo 4: Detectando as peças no tabuleiro

Recebe a lista de peças detectadas e o tabuleiro (matriz de quadrados) para que sejam detectadas **as posições de cada peça em um determinado quadrado**.

```python

class ChessObject:
    top_left: tuple[int, int] # Recebe como (x,y)
    top_right: tuple[int, int]
    bottom_right: tuple[int, int]
    bottom_left: tuple[int, int]
    #...

class Piece(ChessObject):
    name: str
    #...

class Square(ChessObject):
    #...
```

```python
# Detectando peças no tabuleiro
board: list[list[ChessObject]] = detect_pieces_in_board(pieces, board)
```

## Passo 5: Detectando posições de uma determinada peça

Para uma determinada peça (obtida no [passo 1](#passo-1-lendo-a-peça-desejada)), iremos detectar suas possíveis posições.

```python
# Buscando a peça desejada no tabuleiro
piece = find_piece_in_board(board, piece_notation)

# Detectando posições de uma peça, caso ela exista no tabuleiro.
if isinstance(piece, Piece):
    positions = list[ChessObject] = detect_positions(board, piece)
```

## Passo 6: Desenhando as posições na imagem

Desenha os contornos nas posições encontradas

```python
# Desenhando as posições na imagem
draw_positions(image, positions)
```

## Código final

```python
class ChessObject:
    top_left: tuple[int, int] # Recebe como (x,y)
    top_right: tuple[int, int]
    bottom_right: tuple[int, int]
    bottom_left: tuple[int, int]
    #...

class Piece(ChessObject):
    name: str
    #...

class Square(ChessObject):
    #...

class Chess:
    def run(self, image):
        piece_notation = input("Digite a peça que você deseja detectar: ")

        # Detectando as peças
        pieces: list[Piece] = detect_pieces(image)

        # Detectando o tabuleiro
        board: list[list[Square]] = detect_board(image)

        # Detectando peças no tabuleiro
        board: list[list[ChessObject]] = detect_pieces_in_board(pieces, board)

        # Buscando a peça desejada no tabuleiro
        piece = find_piece_in_board(board, piece_notation)

        # Detectando posições de uma peça, caso ela exista no tabuleiro.
        if isinstance(piece, Piece):
            positions = list[ChessObject] = detect_positions(board, piece)

            # Desenhando as posições na imagem
            draw_positions(image, positions)

```

## Autores

|                                                       | Colaborador                                          |                                                             | Colaborador                                      |
| ----------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------ |
| ![](https://github.com/artuguen28.png?size=80)        | [Arthur Uguen](https://github.com/artuguen28)        | ![](https://github.com/Gtapajos.png?size=80)                | [Guilherme Tapajós](https://github.com/Gtapajos) |
| ![](https://github.com/FMAbr.png?size=80)             | [Felipe Muniz](https://github.com/FMAbr)             | <img src="https://github.com/melinnediniz.png" width="80"/> | [Melinne Diniz](https://github.com/melinnediniz) |
| ![](https://github.com/gabrielSantosLima.png?size=80) | [Gabriel Lima](https://github.com/gabrielSantosLima) | ![](https://github.com/tfarias88.png?size=80)               | [Tiago Farias](https://github.com/tfarias88)     |
