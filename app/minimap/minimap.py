import cv2
import numpy as np
from app.managers import WindowManager

def create_chessboard_image(size = (50, 50)):
    white_square = np.full(size, 255, dtype=np.uint8)
    black_square = np.zeros(size, np.uint8)

    coordinates = []
    image = np.zeros((400, 400), dtype=np.uint8)
    i = 1
    for y in range(0, 400, 50):
        i = 1 - i
        row = []
        for x in range(0, 400, 50):
            row.append((slice(y, y+50), slice(x, x+50), slice(3)))
            if (x//10) % 2 == i:
                image[y:y+50, x:x+50] = white_square
        coordinates.append(row)

    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    return image, coordinates

def paint_square(coordinates, color = (0, 128, 0)):
    for coord in coordinates:
        y, x = coord
        board_map[board_coordinates[y][x]] = np.full((50, 50, 3), color, dtype=np.uint8)

class Minimap():
    def __init__(self, name, size):
        self.name = name
        self._isWindowCreated = False

        image, coordinates = create_chessboard_image(size)
        self._clear = image        
        self._image = image.copy()
        self._coordinates = coordinates

    def show(self):
        if not self._isWindowCreated:
            self._window = cv2.namedWindow(self.name)
            self._isWindowCreated = True
        
        cv2.imshow(self.name, self._image)       

    def hide(self):
        cv2.destroyWindow(self.name)
        self._isWindowCreated = False

    def update(self):
        if self._isWindowCreated:
            cv2.imshow(self.name, self._image)       

    def paint_squares(self, coordinates, color = (0, 128, 0)):
        self._image = self._clear.copy()
        for coord in coordinates:
            y, x = coord
            self._image[self._coordinates[y][x]] = np.full((50, 50, 3), color, dtype=np.uint8)
        self.update()

    def clear(self):
        self._image = self._clear.copy()
        self.update()  

