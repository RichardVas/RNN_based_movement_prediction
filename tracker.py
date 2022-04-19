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
        self.center_points = {}
        #redundant
        self.everyCenters = {}
        #id assignment
        self.id_count = 0
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

    def update(self, objects_rect):
        #tracked objs with ids
        objects_bbs_ids = []
        unique_ids = []

        actualID_set = set()

        for rect in objects_rect:
            x, y, w, h = rect
            cx, cy = self.calCenterPoint(x,y,w,h)

            same_object_detected = False

            

            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                #found the same ojb
                if dist <= 25:
                    self.center_points[id] = (cx, cy)

                    self.everyCenters[id] = [cx,cy]
                    #print(self.center_points)
                   # currentobj = self.detectedOBJ[id]

                    objects_bbs_ids.append([x, y, w, h, id])
                    self.detectedOBJ[id].append([x,y,w,h])
                    #self.detectedOBJ[id].append([x,y,w,h])
                    same_object_detected = True
                    actualID_set.add(id)
                    break

            #new object
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                self.everyCenters[self.id_count] = (cx,cy)


                objects_bbs_ids.append([x, y, w, h, self.id_count])
                #dic obj
                self.detectedOBJ[self.id_count]=[[x,y,w,h]]
                #self.detectedOBJ[self.id_count]=[[x,y,w,h]]
                self.id_count += 1
                unique_ids.append(self.id_count)
                self.uniqueIDSET[self.id_count] = self.genRandomGreen()
                actualID_set.add(self.id_count)

       #clean center dict from ununsed ids
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

            ######################################
            nx,ny,nw,nh,nID = obj_bb_id

            

 #       for key in self.detectedOBJ.copy():
 #           if key not in actualID_set:
 #               del self.detectedOBJ[key]

        self.center_points = new_center_points.copy()

        return objects_bbs_ids, unique_ids
    


            


