from imghdr import what
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_pdf import PdfPages, PdfFile


class Grapher():
    def __init__(self):
#        super(Grapher, self).__init__()
        #todo
        #given an 2d array
        #convert ot np array
        #transpose
        #scatter then plot, finally show the whole
#        pass


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
        #plt.legend(['Plot 1', 'Plot 2'])   
        # 
      #  pdf = matplotlib.backends.backend_pdf.PdfPages("output.pdf")
        
        plt.savefig('asd.png')     
        plt.show()

    def displayGraph2(self):
        #parse the base of arrays and for each elemnt export the plts
        fig, (ax1,ax2) = plt.subplot(1,2)
        for i in self.base:
            tmp = np.array(i)
            tmp = tmp.T
            plt.scatter(tmp[0],tmp[1])

            plt.plot(tmp[0],tmp[1])
        #plt.legend(['Plot 1', 'Plot 2'])   
        # 
      #  pdf = matplotlib.backends.backend_pdf.PdfPages("output.pdf")
        
        plt.savefig('asd.png')     
        plt.show()

    def display2(self):
        #feladat: hozzunk letre dinamikusan iterlhato tengelyeket listajat, annyi tengely legyen mint elem a self.baseben
        # ezt egyszerre iteraljuk vegig a self.basel és az aktuális elemet az aktuális tengelyre rakom
        #ez
        fig, ax = plt.subplots(nrows=12, ncols=2)
        
        plt.tight_layout()
       # fig, [ax1, ax2] = plt.subplots(len(self.base))
        i= 0
        for row in ax:
            for col in row:
                tmp = np.array(self.base[i])
                tmp = tmp.T
            #fig, [ax1, ax2] = plt.subplots(len(self.base))
                col.scatter(tmp[0],tmp[1])
                col.plot(tmp[0],tmp[1])

      #          tmp2 = np.array(self.base[i+1])
      #          tmp2 = tmp2.T
      #          col.scatter(tmp2[0],tmp2[1])
      #          col.plot(tmp2[0],tmp2[1])
#itt csak simán hozzadaom a prediktált értékekeket
#                col.scatter([69],[69])
#                col.plot([69],[69])

                i+= 1
               # i+= 2
          #  ax2.plot(tmp)
          #  ax3.plot(tmp)
                plt.rcParams['pdf.fonttype'] = 42
                plt.rcParams['font.family'] = 'Calibri'
    # with PdfPages('test.pdf') as pdf:
        #fig.savefig("bruh.pdf",bbox_inches = 'tight')

                pp = PdfPages('foo.pdf')
                pp.savefig(col)
        #      pp.savefig(plot2)
        #      pp.savefig(plot3)
                pp.close()

        plt.show()

    def addDict(self,key,value):
        self.dictGroup[key] = value
   
    def addDict2(self,input_dict):
        for key in input_dict:
            self.dictGroup[key] = input_dict[key]

    def displayFromDict2(self):
        arrOfLegends = []
        for i in self.dictGroup:
           # print(self.dictGroup[i])
            tmp = np.array(self.dictGroup[i])
            tmp = tmp.T
            print('tmp',tmp[0])
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
       # plt.legend(arrOfLegends)
       # plt.show()

    def save_multi_image(self,inp,pred,key):
        plt.rcParams['pdf.fonttype'] = 42
        plt.rcParams['font.family'] = 'Calibri'

        fig1 = plt.figure()
        plt.title('original')
        tmp = np.array(inp)
    #    print('original',tmp)
        tmp = tmp.T
        plt.scatter(tmp[0],tmp[1],color = 'green')
        plt.plot(tmp[0],tmp[1],  color='green', lw=2)
       # plt.plot([2, 1, 7, 1, 2], color='red', lw=5)

        fig2 = plt.figure()
        plt.title('predicted')
        whatisit = inp
       #đ whatisit[-1] = [pred]
      #  print('pred',whatisit)
        tmppred = np.array(pred)
        tmppred = tmppred.T
        plt.scatter(tmppred[0],tmppred[1],color = 'red')
        plt.plot(tmppred[0],tmppred[1], color='red', lw=2)

        #plt.show()
        pp = PdfPages("./test_graphs/asd0410{}.pdf".format(key))
        fig_nums = plt.get_fignums()
        figs = [plt.figure(n) for n in fig_nums]
        for fig in figs:
            fig.savefig(pp, format='pdf')
        pp.close()



    


if __name__ == "__main__":
    displayer = Grapher()


    bla = [[10, 20], [20, 30], [40, 50]]
    qwe = [[1,2],[2,3],[4,5]]
   # qwe = [[]]
   # displayer.addArray(qwe)
    #displayer.displayGraph()
    displayer.save_multi_image(bla, qwe)
   # asd = [[4,5],[5,3],[9,5]]
    
   # blaasd = [[10, 20], [20, 30], [40, 50]]
 #   displayer.addArray(qwe)
 #   displayer.addArray(asd)
 #   displayer.addArray(bla)
 #   displayer.addArray(qwe)
   # displayer.displayGraph()
 #   displayer.display2()
#fig, axs = plt.subplots()
#fig.suptitle('Vertically stacked subplots')
#axs[0].plot(x, y)
#axs[1].plot(x, -y)