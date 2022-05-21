import numpy as np
from sklearn.preprocessing import MinMaxScaler
from grapher import *


class Dataset():

    # generate dataset from 0 koord
    def generateSeq(self,seq_len):
        dataset = []
        # bal also sarok
        b1 = ([[i,0] for i in range (seq_len)]) # x tengely +

        b2 = [[0,i] for i in range (seq_len)] # y tengely +

        b3 = [[i,i] for i in range (seq_len)] # x,y +

        b4 = [[i,i/2] for i in range (seq_len)]

        b5 = [[i/2,i] for i in range (seq_len)]




        #jobb also
        j1 = [i for i in b1[::-1]] # inverze x
        j2 = [[seq_len-1-i,i] for i in range(seq_len)] # atlo
        j3 = [[seq_len-1,i] for i in range(seq_len)] # fugg no
        j4 = [[seq_len-1-i,i/2] for i in range(seq_len)] # atlo
        j5 = [[seq_len-1-i/2,i] for i in range(seq_len)] # atlo


        #jobb felso
        jf1 = [[seq_len-1-i,seq_len-1] for i in range(seq_len)]
        jf2 = [[seq_len-1,seq_len-1-i] for i in range(seq_len)]
        jf3 = [[seq_len-1-i,seq_len-1-i] for i in range(seq_len)]
        jf4 = [[seq_len-1-i/2, seq_len-1-i] for i in range(seq_len)]
        jf5 = [[seq_len-1-i, seq_len-1-i/2] for i in range(seq_len)]




        #bal felso
        bf1 = [[i,seq_len-1] for i in range(seq_len)]
        bf2 = [[0,seq_len-1-i] for i in range(seq_len)]
        bf3 = [[i,seq_len-1-i] for i in range(seq_len)]
        bf4 = [[i/2,seq_len-1-i] for i in range(seq_len)]
        bf5 = [[i,seq_len-1-i/2] for i in range(seq_len)]


        agg_dataset = [b1,b2,b3,b4,b5,j1,j2,j3,j4,j5,jf1,jf2,jf3,jf4,jf5,bf1,bf2,bf3,bf4,bf5]
        big_array =[]
        for i in agg_dataset:
            for j in i:
                big_array.append(j)
        return big_array
    def __init__(self, max_size):

        #self.max_size = max_size
        self.dataset = self.generateSeq(max_size)
       # self.shape = self.dataset.shape
        self.length = len(self.dataset)
        self.inp_feature = 2
        self.steps_forward = 3





if __name__ == "__main__":
    dat = Dataset(12)
    app = dat.dataset
    print(app)
    viz = Grapher()
    viz.addArray(app)
    viz.displayGraph()

    scaler = MinMaxScaler()

    dataset = scaler.fit_transform(app)
    seq_len = 13
    input_feature = 2
    dataset = dataset.reshape(-1, seq_len*input_feature)
    print(dataset)
