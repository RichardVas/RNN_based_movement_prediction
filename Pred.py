import torch.optim
from os.path import exists

from LSTM import *
from dataset import *
# from torch.utils.tensorboard import SummaryWriter
import math
from time import strftime, time
from datetime import datetime


import matplotlib.pyplot as plt

from grapher import *

from dataset import *




class Predictor():
    def __init__(self):
        super(Predictor, self).__init__()
        self.model = LSTM(2, 16, 1).to(dev) # LSTM hálózat példányosítása
        self.scaler = MinMaxScaler() #szükséges skálázó függvény implementálása
        self.unscaled_dataset= Dataset(13) # dataset betöltése, 
        self.app = np.array(self.unscaled_dataset.dataset)
        self.features = self.scaler.fit(self.app)
        self.dataset = self.scaler.transform(self.app) #
        self.seq_len = 13 #0 miatt 1el novelni a kivant seq_lent
        self.input_feature = self.unscaled_dataset.inp_feature # amennyiben 2d koordinatarendszert hasznalok mindig 2
        self.dataset = self.dataset.reshape(-1, self.seq_len*self.input_feature) # skalazott adathalmaz 'bach'-ekre bontva
        self.batch_size = self.dataset.shape[0]
        self.PATH = 'trained_models/20220501_17535720220427_1712243stepsforward.pth'
       # self.PATH = 'untrained_model.pth'
        self.load_model = exists(self.PATH)
        # lehetőség van korábban tanított hálózat betöltésére.
        if (self.load_model):
            self.model.load_state_dict(torch.load(self.PATH))
            self.model.eval()
        self.input_tensor = np.array([])
        self.target_tensor = np.array([])

    # hálózatot betanító metódus
    def train(self):
        if (self.load_model is False):
            n_batches = self.batch_size
            seq_len = 10 # hálózatnak inputként adott vector hossza
            input_feature = self.input_feature #a kapott input vektor dimenziója
            losses = [] # egyes veszteségek nyilvántartására szolgáló lista
            torch.manual_seed(1)
            # input és target tensorok számára létrehozott, és átcastolt numpy tömbök
            inp = np.array(self.dataset[:, :-6]).astype(np.float32)
            tar = np.array(self.dataset[:, 6:]).astype(np.float32)
            # tensorok létrehozása numpy tömbökből, GPU-nak átadni őket.
            self.input_tensor = torch.from_numpy(inp).reshape(n_batches, seq_len, input_feature).to(dev)
            self.target_tensor = torch.from_numpy(tar).reshape(n_batches, seq_len, input_feature).to(dev)

            # Adam optimizer számára paraméterek szolgáltatása
            optimizer = torch.optim.Adam(self.model.parameters(), lr=0.1)
            # a tanítás továbbí paraméterei
            loss = nn.MSELoss()
            epoch = 2501
            self.model.train()
            for i in range(epoch):

                optimizer.zero_grad()
                x = self.model.forward(self.input_tensor)
                single_loss = loss(x, self.target_tensor)
                losses.append(single_loss)
                if (i % 100 == 0):
                    print('epoch: ', i, 'loss:', single_loss)
                # gradiensek számítása
                single_loss.backward()
                # súlyok frissítése
                optimizer.step()
            # training végén eredmény, megjelenítése, modell mentése
            timestr = datetime.now().strftime("%Y%m%d_%H%M%S")
            plt.plot(losses)
            title = 'train_losses/{}'.format(timestr+self.PATH)
            plt.title(title)
            plt.savefig(title+'.jpg')
            
            torch.save(self.model.state_dict(), 'trained_models/'+timestr + self.PATH)
            print('Training is done: modelPTH: ','trained_models/'+timestr + self.PATH)

           
        else:
            print('Model is already trained via: ',self.PATH)
    #képzes végén beállítja a konstruktorban definiált hállózat paramétereit.
    # metódus, amivel a tanított hálózatnak inputokat adhatok, jóslás érdekében.
    def predict(self, input_vector):
        self.model.eval()

        input_vector = self.scaler.transform(input_vector)
        with torch.no_grad():
            # assuem that the input is correctly shaped
            inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
            er = self.scaler.inverse_transform(result.cpu().data.view(-1, 2))

           # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
           # print(toreturn)
            return er[-1]
           # return toreturn
    # kapott inputra visszatér annak predikciójával.
    def predict2(self, input_vector):
        self.model.eval()

        scalerr = MinMaxScaler()
        scalerr.fit(input_vector)
        input_vector = self.scaler.transform(input_vector)
        with torch.no_grad():
            # assuem that the input is correctly shaped
            # inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
            er = scalerr.inverse_transform(result.cpu().data.view(-1, 2))

           # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
           # print(toreturn)
            return er[-1]
           # return toreturn

    def predict3(self, input_vector):
        self.model.eval()

        scalerr = MinMaxScaler()
        
        scalerr.fit(input_vector)
        input_vector =scalerr.transform(input_vector)
        
      #  print('inputvector',input_vector)
        with torch.no_grad():
            # assuem that the input is correctly shaped
            # inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
         #   print('result',result)
            er = scalerr.inverse_transform(result.cpu().data.view(-1, 2))
            
           # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
           # print(toreturn)
            return er[-1]
           # return toreturn
           
    def predict4(self, input_vector):
        self.model.eval()

      #  print('akt featurok',self.features)
        scalerr = MinMaxScaler(feature_range= (0,10))
      #  print(input_vector)
       # scalerr = MinMaxScaler(feature_range= (-10,10))
        #scalerr = MinMaxScaler(feature_range= (0,10))
        
        scalerr.fit(input_vector)
        input_vector =scalerr.transform(input_vector)
      #  print('input_vector',input_vector)
        input_vector = self.scaler.transform(input_vector)
        
       # print('inputvector',input_vector)
        with torch.no_grad():
            # assuem that the input is correctly shaped
            # inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
        #    print('result',result)
            er = self.scaler.inverse_transform(result.cpu().data.view(-1, 2))

            er = scalerr.inverse_transform(er)
            
           # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
           # print(toreturn)
            
           # return er[-3:]
            return er[-1]
           # return toreturn
    def predict5(self, input_vector):
        self.model.eval()
        lix = input_vector[-1][0]
        liy = input_vector[-1][1]
        last = abs(lix) + abs(liy)
        fix = input_vector[0][0]
        fiy = input_vector[0][1]
        first = abs(fix) + abs(fiy)

   #     print('jkl',lix,liy)
        if(first < last):
    #        novekvo
            scalerr = MinMaxScaler(feature_range= (3,12))
        else:
     #       csokkeno
            scalerr = MinMaxScaler(feature_range= (0,9))

        
        scalerr.fit(input_vector)
        input_vector =scalerr.transform(input_vector)
        #  print('input_vector',input_vector)
        input_vector = self.scaler.transform(input_vector)
        
        # print('inputvector',input_vector)
        with torch.no_grad():
            # assuem that the input is correctly shaped
            # inp = self.scaler.fit_transform(input_vector)
            inp_tensor = torch.FloatTensor(input_vector).reshape(1, len(input_vector), 2).to(dev)
            result = self.model.forward(inp_tensor)
        #    print('result',result)
            er = self.scaler.inverse_transform(result.cpu().data.view(-1, 2))

            er = scalerr.inverse_transform(er)
            
            # toreturn = (roundToInt(er[-1][0]), roundToInt(er[-1][1]))
            # print(toreturn)
            
            # return er[-3:]
            return er[-1]
        # return toreturn



    def roundToInt(self,x):
        return int(x + math.copysign(0.5, x))


if __name__ == "__main__":
    test_model = Predictor()
    test_model.train()