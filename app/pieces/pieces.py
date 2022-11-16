import cv2
from app.chesspiece import Piece


def detection_2_pieces(detect, model):
	pieces = []
	for det in detect:
		x,y,x2,y2 = det[:4]
		names = model.class_names
		top_left = (x, y)
		bottom_left = (x, y2)
		top_right = (x2, y)
		bottom_right = (x2, y2)

		piece_on_screeen = Piece(top_left, top_right, bottom_right, bottom_left, names[int(det[5])])

		print(f'| {piece_on_screeen.name} |\n   top left: {piece_on_screeen.top_left}   top right: {piece_on_screeen.top_right}')
		print(f'bottom left: {piece_on_screeen.bottom_left} bottom right: {piece_on_screeen.bottom_right}')
		print(f'height: {piece_on_screeen.height}, width: {piece_on_screeen.width}')
		pieces.append(piece_on_screeen)
	return pieces

def detect_pieces(image, model) -> list[Piece]:
	image_display = image.copy()
	image_display = cv2.cvtColor(image_display, cv2.COLOR_BGR2RGB)
	detect = model.processFrame(image_display)
	pieces = detection_2_pieces(detect, model)
	return pieces 