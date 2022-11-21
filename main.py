from app.yolov7_model import yolov7_model
from app.cameo import Cameo
from chess import Chess


model = yolov7_model('./best.pt',conf_thres = 0.20,iou_thres = 0.40)
chess = Chess(model)
cameo = Cameo(chess)
cameo.run()
# cameo.run()