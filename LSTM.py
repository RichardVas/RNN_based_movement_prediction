import torch
import torch.nn as nn
from torch import autograd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

if torch.cuda.is_available():
    dev = "cuda:0"
else:
    dev = "cpu"


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(LSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.lstm1 = nn.LSTM(
            self.input_size,
            self.hidden_size,
            self.num_layers,
            batch_first=True,
            # dropout  = 1
        )

        self.fc = nn.Linear(hidden_size, input_size)

    def forward(self, x):
        # len(x) = batches = 1 , seqlen
        # print(len(x))
        h0 = torch.zeros(self.num_layers, len(x), self.hidden_size).to(dev)
        c0 = torch.zeros(self.num_layers, len(x), self.hidden_size).to(dev)

        out, hn = self.lstm1(x, (h0, c0))

        # return out
        return self.fc(out)
        # return self.fc(out[:,-1,:])

