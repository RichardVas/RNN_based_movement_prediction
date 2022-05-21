from imghdr import what
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_pdf import PdfPages, PdfFile


class Grapher():
    def __init__(self):
        self.base=[]
#        self.fig, self.axs = plt.subplots()
        self.dictGroup={}
    def addArray(self,arr):
        self.base.append(arr)

    def displayGraph(self):
        #parse the base of arrays and for each elemnt export the plts
        for i in self.base:
            tmp = np.array(i)
            tmp = tmp.T
            plt.scatter(tmp[0],tmp[1])

            plt.plot(tmp[0],tmp[1])
        
        plt.savefig('graph.png')     
        plt.show()




    def addDict(self,key,value):
        self.dictGroup[key] = value
   
    def addDict2(self,input_dict):
        for key in input_dict:
            self.dictGroup[key] = input_dict[key]

    def displayFromDict2(self):
        arrOfLegends = []
        for i in self.dictGroup:
            tmp = np.array(self.dictGroup[i])
            tmp = tmp.T

            plt.scatter(tmp[0],tmp[1])
            plt.plot(tmp[0],tmp[1])
            arrOfLegends.append(i)
        plt.legend(arrOfLegends)
        plt.show()

    def displayFromDict(self):
        arrOfLegends = []
        for i in self.dictGroup:
            tmp = np.array(self.dictGroup[i])
            self.addArray(tmp)
            arrOfLegends.append(i)
        self.displayGraph()






    

