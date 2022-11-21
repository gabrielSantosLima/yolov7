import cv2
import numpy as np
from app.chesspiece import Square

SHARPEN_MATRIX = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
color = lambda: list(np.random.random(size=3) * 256)

def adjust_size(image, new_width):
    height, width = image.shape[:2]
    ratio = float(new_width) / width
    
    new_height = int(height * ratio)
    
    image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return image, ratio

def translate_contours(contours, ratio):
    return [np.array([[(np.array(point[0])*ratio).astype(int)] for point in contour]) for contour in contours]

def is_approx_square(contour, percent):
    bounds = cv2.minAreaRect(contour)
    width, height = bounds[1]
    
    return width*(1-percent) <= height <= width*(1+percent)

def square_contours(contours, percent = 0.25):
    return [np.int0(cv2.boxPoints(cv2.minAreaRect(contour))) for contour in contours if is_approx_square(contour, percent)]

def prepare_image(image, area = None, morph = False, sharpen = False):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    if sharpen:
        img_blurred = cv2.medianBlur(img_gray, 5)
        img_sharpened = cv2.filter2D(img_blurred, -1, SHARPEN_MATRIX)
        img_gray = img_sharpened

    img_bin = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 20)
        
    if morph:
        img_bin = cv2.erode(img_bin, np.ones((3,3), np.uint8), iterations=1)

    return img_bin

def find_contours(img_bin, area = None):
    contours = cv2.findContours(img_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]

    if area is not None:
        contours = list(filter(lambda contour: area[0] < cv2.contourArea(contour) < area[1], contours))

    return contours

def create_board(squares: list[Square]):
    qtd = len(squares)

    if qtd == 64:
        print(f'Não é possivel montar o tabuleiro com {qtd} posições.')
        return

    squares.sort(key=lambda square: square.top_left[1])

    board = [squares[i:i+8] for i in range(0, 64, 8)]

    for row in board:
        row.sort(key=lambda square: square.top_left[0])
    
    return board

def detect_board(image, area = (200, 10000), output = None):
    width = image.shape[1]
    height = image.shape[0]
    print(f"{width}x{height}")
    ratio = None
    if width > 1200:
        image, ratio = adjust_size(image, 800)
    
    img_bin = prepare_image(image, morph=True, sharpen=True)

    contours = find_contours(img_bin, area)
    
    print(f'Foram detectados {len(contours)} contornos na imagem')
    if ratio is not None:
        contours = translate_contours(contours, (1/ratio))
    
    contours = square_contours(contours, 0.6)

    if isinstance(output, str) and output:
        file = image.copy()
        for index in range(len(contours)):
            cv2.drawContours(file, contours, index, color(), 5)
        cv2.imwrite(output, file)
    
    squares = []
    for contour in contours:
        bottom_left, top_left, top_right, bottom_right = contour
        squares.append(Square(top_left, top_right, bottom_right, bottom_left))

    print(f'Foram detectados {len(squares)} quadrados na imagem.')

    board = create_board(squares)

    return board
    