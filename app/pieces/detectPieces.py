import cv2
import torch
from app.yolov7_model import yolov7_model
from app.cameo import Cameo
from app.pieces.piece import Piece


class DetectPieces:

	def __init__(self, model):
		self.model = model
		self.pieces = []

	def labelDraw(self, detect):
		pieces = []
		for det in detect:
			x,y,x2,y2 = det[:4]
			#cv2.rectangle(image, (int(x) , int(y)), (int(x2) , int(y2)), color_rec, rec_width)
			names = self.model.class_names
			label = f"{names[int(det[5])]}"
			#cv2.putText(image,label,(int(x),int(y)),font,width_font,color_font)

			piece_on_screeen = Piece(x, y, x2, y2, names[int(det[5])])
			#print(f'{piece_on_screeen.name} |  X: {piece_on_screeen.top_left} X2: {piece_on_screeen.bottom_left}')
			#print(f'Y: {piece_on_screeen.top_right} Y2: {piece_on_screeen.bottom_right}')
			#print(f'height: {piece_on_screeen.height}, width: {piece_on_screeen.width}')
			pieces.append(piece_on_screeen)
		
		return pieces

			

	def onImage(self, imagem_path):
		image = cv2.imread(imagem_path)
		assert image is not None, 'Image Not Found' + imagem_path
		image_display = image.copy()
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		img_size = image.shape
		
		detect = self.model.processFrame(image)
		self.labelDraw(detect)
		return image_display
		

	def detect_pieces(self, image):
		image_display = image.copy()
		image_display = cv2.cvtColor(image_display, cv2.COLOR_BGR2RGB)
		
		detect = self.model.processFrame(image_display)

		self.pieces = self.labelDraw(detect)
		#print(self.pieces)

		return self.pieces 