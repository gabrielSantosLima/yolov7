import cv2
import torch
from app.yolov7_model import yolov7_model
from app.cameo import Cameo
from app.pieces.piece import Piece
from app.pieces.detectPieces import DetectPieces

if __name__ == '__main__':
    model = yolov7_model('./best.pt',conf_thres = 0.20,iou_thres = 0.40)
    main = DetectPieces(model)
    c = Cameo()
    c.run(main)