import torch
import cv2
from app.interfaces.yolov7_model import yolov7_model

def labelDraw(image,detect, color_rec = (255, 255, 0), rec_width = 2, font = cv2.FONT_HERSHEY_COMPLEX_SMALL, width_font = 0.5, color_font = (255,0,0)):
	for det in detect:
		x,y,x2,y2 = det[:4]
		cv2.rectangle(image, (int(x) , int(y)), (int(x2) , int(y2)), color_rec, rec_width)
		names = model.class_names
		label = "Class {0}, conf {conf:.2f}".format(names[int(det[5])],conf = det[4])
		cv2.putText(image,label,(int(x),int(y)),font,width_font,color_font)

def onImage(imagem_path):
	image = cv2.imread(imagem_path)
	assert image is not None, 'Image Not Found' + imagem_path
	image_display = image.copy()
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	img_size = image.shape
	
	detect = model.processFrame(image)
	labelDraw(image_display,detect)
	cv2.imshow("Result", image_display)
	cv2.waitKey(0)


if __name__ == '__main__':
	print("teste")
	model = yolov7_model('best.pt',conf_thres = 0.20,iou_thres = 0.40)
# Formatos de aceitos
	img_formats = ['bmp', 'jpg', 'jpeg','png','tiff','webp','mpo'] # Formato de imagens aceitos
	vid_formats = ['mov','avi','mp4','mpg','m4v','wmv','mkv']      # Formado de videos aceitos
	with torch.no_grad():
		image_source = 'face_teste.jpg'
		if image_source.split('.')[-1].lower() in img_formats:
			onImage(image_source)
	