from collections import defaultdict
import math
import numpy as np
from Pred import *

import json
import csv
import pickle
from random import randint

pred = Predictor()

class EuclideanTracker:
    def __init__(self):
        #needed for euclidean
        self.current_centers = {}
        #redundant
        self.everyCenters = {}
        #id assignment
        self.id_counter = 0
        #overall storage
        self.detectedOBJ = defaultdict(list)
        #easier to find colors
        self.uniqueIDSET = defaultdict(tuple)

    def genRandomGreen(self):
        greenval = randint(100, 255)
        redval = randint(20,(greenval - 60))
        blueval = randint((redval - 20), (redval + 20))
        color = (redval, greenval, blueval)
        
        return color
    #save pickle and humanly readable logs
    def printobjs(self):

        with open('dict1.csv','w') as csv_file:
            writer = csv.writer(csv_file)
            for key,value in self.detectedOBJ.items():
                writer.writerow([key,value])

        with open ('dict.json', 'w', encoding='utf-8') as f:
            json.dump(self.detectedOBJ,f,ensure_ascii=False, indent = 4)

        with open('saved_dictionary.pkl', 'wb') as f:
            pickle.dump(self.detectedOBJ, f)
            
            
    def calCenterPoint(self,x,y,w,h):
            cx = (x + w) / 2 
            cy = (y + h) / 2 

            return cx,cy

    def update(self, detected_obj_list):
        #tracked objs with ids
        objects_bbs_ids = []
        unique_ids = []

        actualID_set = set()

        for current_obj in detected_obj_list:
            x, y, w, h = current_obj

            cx, cy = self.calCenterPoint(x,y,w,h)

            isSameObj = False

            #vegig parzolja a a jelenlegi kozeppontok listajat
           # for id, pt in self.current_centers.items():
            for id in self.current_centers:
                pt = self.current_centers[id]    
                dist = math.hypot(cx - pt[0], cy - pt[1])
                
                #dist <= 25: lehet ha statikus a kamera
                if dist <= 65:

                    self.current_centers[id] = (cx, cy)

                    self.everyCenters[id] = [cx,cy]

                    objects_bbs_ids.append([x, y, w, h, id])
                    self.detectedOBJ[id].append([x,y,w,h])
                    isSameObj = True
                    actualID_set.add(id)
                    break

            #new object
            if isSameObj is False:
                self.current_centers[self.id_counter] = (cx, cy)
                self.everyCenters[self.id_counter] = (cx,cy)


                objects_bbs_ids.append([x, y, w, h, self.id_counter])
                #dic obj
                self.detectedOBJ[self.id_counter]=[[x,y,w,h]]
                self.id_counter += 1
                unique_ids.append(self.id_counter)
                self.uniqueIDSET[self.id_counter] = self.genRandomGreen()
                actualID_set.add(self.id_counter)

       #map takaritasa a nem aktualis idktol
       # kell a következo ciklusban az osszehasonlitasho
        new_current_centers = {}
        for obj_bb_id in objects_bbs_ids:
            dc1, dc2, dc3, dc4, object_id = obj_bb_id
            center = self.current_centers[object_id]
            new_current_centers[object_id] = center

            ######################################
            nx,ny,nw,nh,nID = obj_bb_id

            
        #ha uriteni akarom a detectedOBJ map-et
        #akkor erdemes ha nem akarok kesobb mereseket vegezni
 #       for key in self.detectedOBJ.copy():
 #           if key not in actualID_set:
 #               del self.detectedOBJ[key]

        self.current_centers = new_current_centers.copy()

        return objects_bbs_ids, unique_ids
    


            

