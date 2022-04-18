import torch
import cv2
import pandas as pd

from tracker import *
from detector import *
from Pred import *


import random

from time import time


class VideoProcessor():
  def __init__(self):
    self.source = 'traffic'
    self.video_source = 'videos/{}.mp4'.format(self.source)
    self.detector = Detector()
    self.tracker = EuclideanTracker()
    self.cap = cv2.VideoCapture(self.video_source)

    self.width= int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    self.height= int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    self.out= cv2.VideoWriter(self.source+'_predicted'+'.mp4', -1, 20.0, (self.width, self.height))


  def DisplayDetectedOBJs(self,frame,detectedOBJs,uniqueIDset):
        for object in detectedOBJs:
      # x,y,w,h,id = box_id
          x = int(object[0])
          y = int(object[1])
          w = int(object[2]-object[0])
          h = int(object[3]-object[1])
          id = object[4]
          color = uniqueIDset[id]
          cv2.putText(frame,str(id),(x,y-15),cv2.FONT_HERSHEY_PLAIN,1,color,2)
          cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)

  def DisplayPredictedOBJs(self,frame,preddict):

    for obj in preddict:
      key = obj
      n,m = preddict[obj]

      cv2.putText(frame,str(key),(n-5,m-5),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
      #cv2.circle(frame,(actx,acty), radius=10, color=(0, 0, 255), thickness=4)
      cv2.rectangle(frame,(n,m),(n+50,m+50),(0,0,255),2)

  def calcDisplacement(self,actx,acty,predx,predy):
      x1 = actx
      y1 = acty
      x2 = predx
      y2 = predy
      dx = x2-x1
      dy = y2-y1
      return dx,dy

# legyen egy prediktáló függvény, ami végig megy a detektált objektumokon és adja vissza az egyes objektumok jövőbeli helyzetét.
  def CreatePredictions(self,frame,frame_counter, detectedOBJs,preddict):

            #start of prediction loop
          for key in detectedOBJs:
              #eloszor nézzük meg minden ID-hez tartozó 2d tömböket
             # print(key,detectedOBJs[key])
              tmp = []
              for i in detectedOBJs[key]:


                
                  tmp.append([i[0],i[1]])
               #   print('i',i)
              #ilyenkor azért prediktál pontosan egyszer mert ha egyszer beölti a6 5öt, akkor prediktál és soha többet nem lesz öt
              #minden 5. elem utan prediktaljon 1et
              

              
              if(len(tmp)>=10 and key in self.tracker.center_points):

                  latest5 = tmp[-10:]


                  

                  
                  actx = latest5[-1][0]
                  acty= latest5[-1][1]

                  testinp = np.array(latest5)

                  testinp = testinp.reshape(-1,2)
                  actual = pred.predict4(testinp)
                  
                  n,m = actual
                  n = pred.roundToInt(n) 
                  m = pred.roundToInt(m)

                  dx,dy = self.calcDisplacement(actx,acty,n,m)



                  o,p =self.tracker.center_points[key]

                  corner_x = 2* o - n + dx*2
                  corner_y = 2* p - m  + dy*2

                  predCenter_x, predCenter_y = self.tracker.calCenterPoint(n,m,corner_x,corner_y)
                  cv2.putText(frame,str(key),(n-5,m-5),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
                  cv2.circle(frame,(int(predCenter_x),int(predCenter_y)), radius=5, color=(0, 0, 255), thickness=2)
                  cv2.rectangle(frame,(n,m),(pred.roundToInt(corner_x),pred.roundToInt(corner_y)),(0,0,255),2)
                  cv2.line(frame,(int(o),int(p)),(int(predCenter_x),int(predCenter_y)),(0,0,255),2) 

  def MainLoop(self):

    ids = []
    frame_counter = 0
    pred_dict = {}
    while True:
        
        start = time()

        ret, frame = self.cap.read()
        frame_counter += 1

        objects_detected = []
        self.detector.forward(frame,objects_detected)

      

        boxes_ids,id_set = self.tracker.update(objects_detected)

        ids.append(id_set)



        OBJs = self.tracker.detectedOBJ

        
        self.DisplayDetectedOBJs(frame,boxes_ids,self.tracker.uniqueIDSET)
        self.CreatePredictions(frame,frame_counter,OBJs,pred_dict)


        end = time()
        #display FPS
        try:
          cv2.putText(frame,'FPS: {}'.format(round(1/(end-start))),(50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
        except ZeroDivisionError :
          
          print('Failed to properly load video or eof.')
          break
        if(ret):
          cv2.imshow("Frames",frame)

        self.out.write(frame)
        key = cv2.waitKey(1)
        if key == 27: 
            self.tracker.printobjs()

            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
  main = VideoProcessor()
  main.MainLoop()