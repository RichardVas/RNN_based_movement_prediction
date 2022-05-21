import torch
import pandas as pd

class Detector():
    def __init__(self):
      #pytorch hubloadon keresztül kívánt méretű hálózat betöltése
      self.yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)
      self.filter = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat']
    def forward(self,frame,objects_detected):
      try:
        results = self.yolo_model(frame)
        df = pd.DataFrame(results.pandas().xyxy[0])
        df = df.query(" name in @self.filter")
        for index, row in df.iterrows():
            #határoló doboz 2 szükséges sarkának koordinátája
            # X - Y - X+W = xmax - Y+H = ymax
            objects_detected.append([row['xmin'],row['ymin'], row['xmax'], row['ymax']])
      except AttributeError:
        print('Failed to load the Frame , missing or obsolete Opencv / video source.'.format(frame))
    
