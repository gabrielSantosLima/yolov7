from app.yolov7_model import yolov7_model
from app.cameo import Cameo
from app.minimap.minimap import Minimap
from chess import Chess


model = yolov7_model('./best.pt',conf_thres = 0.20,iou_thres = 0.40)
mp = Minimap('Movimentos', (50, 50))
chess = Chess(model, mp)
cameo = Cameo(chess)
cameo.run(chess)
# cameo.run()