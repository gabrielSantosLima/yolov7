import cv2
import numpy as np

# exemplo
#    x1, y1    x2, y2     x3,  y3    x4,  y4
# [[50, 50], [250, 50], [250, 200], [50, 200]]

def draw_positions(image, chessObject_list):
    img = image.copy()
    for chessObject in chessObject_list:
        contours = [chessObject.top_left, 
                    chessObject.top_right,
                    chessObject.bottom_right,
                    chessObject.bottom_left]
        points = np.array([contours])
        cv2.drawContours(img, points, 0, (128, 255, 0), 3)
    return img