import cv2
import torch
from app import yolov7_model, cameo, piece


class DetectPieces:

	def __init__(self, model):
		self.model = model
		self.pieces = []

	def labelDraw(self, image,detect, color_rec = (255, 255, 0), rec_width = 2, font = cv2.FONT_HERSHEY_COMPLEX_SMALL, width_font = 0.5, color_font = (255,0,0)):
		pieces = []
		for det in detect:
			x,y,x2,y2 = det[:4]
			cv2.rectangle(image, (int(x) , int(y)), (int(x2) , int(y2)), color_rec, rec_width)
			names = self.model.class_names
			label = f"{names[int(det[5])]}"
			cv2.putText(image,label,(int(x),int(y)),font,width_font,color_font)

			piece_on_screeen = piece.Piece(x, y, x2, y2, names[int(det[5])])
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
		self.labelDraw(image_display,detect)
		return image_display
		

	def detect_pieces(self, image):
		image_display = image.copy()
		image_display = cv2.cvtColor(image_display, cv2.COLOR_BGR2RGB)
		
		detect = self.model.processFrame(image_display)

		self.pieces = self.labelDraw(image,detect)
		#print(self.pieces)

		return self.pieces 
	
	



'''if __name__ == '__main__':
# Formatos de aceitos
	model = yolov7_model.yolov7_model('./best.pt',conf_thres = 0.20,iou_thres = 0.40)
	img_formats = ['bmp', 'jpg', 'jpeg','png','tiff','webp','mpo'] # Formato de imagens aceitos
	vid_formats = ['mov','avi','mp4','mpg','m4v','wmv','mkv']      # Formado de videos aceitos
	main = Main(model)
	with torch.no_grad():
		image_source = './screenshot.png'
		if image_source.split('.')[-1].lower() in img_formats:
			a = main.onImage(image_source)
			cv2.imshow("Result", a)
			cv2.waitKey(0)'''

if __name__ == '__main__':
    model = yolov7_model.yolov7_model('./best.pt',conf_thres = 0.20,iou_thres = 0.40)
    main = DetectPieces(model)
    c = cameo.Cameo()
    c.run(main)