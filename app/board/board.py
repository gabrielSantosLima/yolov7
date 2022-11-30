import cv2
import numpy as np
from app.chesspiece import Square

SHARPEN_MATRIX = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
color = lambda: list(np.random.random(size=3) * 256)
def square_contours(contours, percent = 0.25):
    squares = []
    for contour in contours:
        x0, y0, width, height = cv2.boundingRect(contour)

        if width*(1-percent) <= height <= width*(1+percent):
            x1, y1 = x0 + width, y0 + height
            squares.append(np.int0([(x0, y1), (x0, y0), (x1, y0), (x1, y1)]))

    return squares

def prepare_image(image, morph = False, sharpen = False):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    if sharpen:
        img_blurred = cv2.medianBlur(img_gray, 5)
        img_sharpened = cv2.filter2D(img_blurred, -1, SHARPEN_MATRIX)
        img_gray = img_sharpened

    img_bin = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 20)
        
    if morph:
        img_bin = cv2.erode(img_bin, np.ones((2,2), np.uint8), iterations=1)

    return img_bin

def find_contours(img_bin, area = None):
    contours = cv2.findContours(img_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]

    if area is not None:
        contours = list(filter(lambda contour: area[0] < np.prod(cv2.boundingRect(contour)[2:]) < area[1], contours))

    return contours

def create_board(squares: list[Square]):
    qtd = len(squares)

    print(f'Foram detectados {qtd} quadrados na imagem.')

    # Ordenando quadrados pela posição vertical (mais a cima primeiro)
    squares.sort(key=lambda square: square.top_left[1])
    print(squares)
    # Metade da altura do quadrado
    row_tresh = (squares[0].bottom_left[1] - squares[0].top_left[1])/2
    print(f'Altura - {row_tresh}')

    rows, columns = [], []
    for index in range(1, len(squares)):
        current, previous = squares[index], squares[index - 1]

        y, y_prev = current.top_left[1], previous.top_left[1]

        # Se a diferença do topo do quadrado atual e do anterior for maior que o treshold, consideramos uma linha nova
        if y - y_prev > row_tresh or index == len(squares)-1:
            print(f'Linha nova ({len(columns)} elementos) <-- {y} - {y_prev} > {row_tresh}')
            rows.append(columns)
            columns = [current]
            row_tresh = (current.bottom_left[1] - current.top_left[1])/2
        # Caso contrário, o elemento é adicionado à linha atual
        else:
            columns.append(current)
    print()

    # Ordenando cada linha pela posição horizontal (mais a esquerda primeiro)
    for row in rows:
        row.sort(key=lambda square: square.top_left[0])
    
    if qtd < 64:
        print(f'Autopreenchendo {64-qtd} quadrados.\n')

        for index, row in enumerate(rows):
            while len(row) < 8:
                # 90% da largura do quadrado
                col_tresh = (row[0].top_right[0] - row[0].top_left[0])*0.9

                for column in range(1, len(row)):
                    current, previous = row[column], row[column - 1]

                    x, x_prev = current.top_left[0], previous.top_left[0]

                    # Se a diferença da esquerda do quadrado atual e a direita do anterior for maior que o treshold, preenchemos a coluna vazia
                    if x - x_prev > col_tresh:
                        print(f'Quadrado novo ([{index}][{column}]) <-- {x} - {x_prev} > {col_tresh}')
                        width = previous.top_right[0] - previous.top_left[0]
                        left, top = previous.top_right
                        right, bottom = left+width, current.bottom_left[1]
                            
                        square = Square((left, top), (right, top), (right, bottom), (left, bottom))

                        row.insert(column, square)
                        break
            print()
    
    return rows

def detect_board(image, area = (20*20, 55*50), output = None):
    img_bin = prepare_image(image, morph=True, sharpen=False)

    contours = find_contours(img_bin, area)
        
    contours = square_contours(contours)

    if isinstance(output, str) and output:
        file = image.copy()
        for index in range(len(contours)):
            cv2.drawContours(file, contours, index, color(), 2)
        cv2.imwrite('bin-' + output, img_bin)
        cv2.imwrite(output, file)
    
    squares = []
    for contour in contours:
        bottom_left, top_left, top_right, bottom_right = contour
        squares.append(Square(top_left, top_right, bottom_right, bottom_left))

    board = create_board(squares)

    return board