
import torch
import cv2
import pandas as pd

from tracker import *
from detector import *
from Pred import *


import random

from time import time

#Képfeldolgozó osztály, a 3 modul
class VideoProcessor():
  def __init__(self):
    self.source = 'varos_2022-03-18_10-53' #input video fájl neve
    #self.source = 'Highway - 20090.mp4'
    #self.video_source = 'Highway - 20090.mp4'
    #inputjaim videos mappában vannak mp4 formátumban
    self.video_source = 'videos/{}.mp4'.format(self.source)
    self.detector = Detector()#Yolo hálózat
    self.tracker = EuclideanTracker()#Tracking modul
    self.cap = cv2.VideoCapture(self.video_source)
    #megjelenítendő Framek tulajdonsága
    self.width= int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    self.height= int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    self.out= cv2.VideoWriter(self.source+'_predicted'+'.mp4', -1, 20.0, (self.width, self.height))
    self.frame_counter = 1

    self.frame_rate_list = []


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
        #  predicted = self.kf.predict(x,y)
        #  cv2.putText(frame,str(id),(predicted[0],predicted[1]-15),cv2.FONT_HERSHEY_PLAIN,1,(100,100,100),2)
        #  cv2.rectangle(frame,(predicted[0],predicted[1]),(predicted[0]+50,predicted[1]+50),(100,100,100),3)

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
              

              
              if(len(tmp)>=10 and key in self.tracker.current_centers):

                  latest10 = tmp[-10:]


                  

                  
                  actx = latest10[-1][0]
                  acty= latest10[-1][1]

                  testinp = np.array(latest10)

                  testinp = testinp.reshape(-1,2)
                  actual = pred.predict4(testinp)
                  
                  n,m = actual
                  n = pred.roundToInt(n) 
                  m = pred.roundToInt(m)

                  dx,dy = self.calcDisplacement(actx,acty,n,m)



                  o,p =self.tracker.current_centers[key]

                  corner_x = 2* o - n + dx*2
                  corner_y = 2* p - m  + dy*2

                  predCenter_x, predCenter_y = self.tracker.calCenterPoint(n,m,corner_x,corner_y)
                  cv2.putText(frame,str(key),(n-5,m-5),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
                  cv2.circle(frame,(int(predCenter_x),int(predCenter_y)), radius=5, color=(0, 0, 255), thickness=2)
                  cv2.rectangle(frame,(n,m),(pred.roundToInt(corner_x),pred.roundToInt(corner_y)),(0,0,255),2)
                  cv2.line(frame,(int(o),int(p)),(int(predCenter_x),int(predCenter_y)),(0,0,255),2) 
                  #cv2.arrowedLine(frame,(int(o),int(p)),(int(predCenter_x),int(predCenter_y)),(0,0,255),5)

  def MainLoop(self):

    ids = []
    self.frame_counter = 0
    pred_dict = {}


    elaps_start = time()
    while True:
        
        start = time()

        ret, frame = self.cap.read()
        self.frame_counter += 1

        objects_detected = []
        self.detector.forward(frame,objects_detected)

      

        boxes_ids,id_set = self.tracker.update(objects_detected)

        ids.append(id_set)



        OBJs = self.tracker.detectedOBJ

        
        self.DisplayDetectedOBJs(frame,boxes_ids,self.tracker.uniqueIDSET)
        self.CreatePredictions(frame,self.frame_counter,OBJs,pred_dict)


        end = time()
        #display FPS
        elapsedT = time() - elaps_start
        try:
          act_FPS = round(1/(end-start))
          cv2.putText(frame,'FPS: {}'.format(act_FPS),(50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
          self.frame_rate_list.append(act_FPS)
          cv2.putText(frame,'Frame: {}'.format(self.frame_counter),(50,75),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
          cv2.putText(frame,'ElapsedT: {}'.format(elapsedT),(50,100),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
          self.frame_counter += 1

        except ZeroDivisionError :
          
          print('Failed to properly load video or eof.')
          ret = False
          print(self.frame_counter)

        self.out.write(frame)
        if(ret):
          cv2.imshow("Frames",frame)
        else:
          self.tracker.printobjs()
          print(self.frame_counter)
          #remove first and last number of framerate, to avoid adding false data
          self.frame_rate_list = self.frame_rate_list[1:-1]
          break


        key = cv2.waitKey(1)
        if key == 27: 
            self.tracker.printobjs()
            print(self.frame_counter)
            break
    

    cv2.destroyAllWindows()


if __name__ == "__main__":
  main = VideoProcessor()
  main.MainLoop()
  plt.plot(main.frame_rate_list)
  plt.title('Atlagos FPS:{}'.format(np.mean(main.frame_rate_list)))
  plt.xlabel('Iterációk')
  plt.ylabel('FrameRate')
  plt.savefig('{}_FPS.jpg'.format(main.source))