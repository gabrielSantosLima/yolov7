import cv2
import numpy as np

white_square = np.full((50, 50), 255, dtype=np.uint8)
black_square = np.zeros((50, 50), np.uint8)
board_row = ((np.indices((1, 8), object).sum(axis=0) + 1) % 2)

board_map = np.zeros((400, 400), dtype=np.uint8)
i = 1
for y in range(0, 400, 50):
    i = 0 if i != 0 else 1
    for x in range(0, 400, 50):
        if (x//10) % 2 == i:
            print(f'WHITE[{y//10}:{y+50}, {x//10}:{x+50}]')
            board_map[y:y+50, x:x+50] = white_square
        else:
            print(f'BLACK[{y//10}:{y+50}, {x//10}:{x+50}]')


# board_map[board_map == 1] = white_square
cv2.imshow('Movimentos', board_map)
cv2.waitKey()
cv2.destroyAllWindows()