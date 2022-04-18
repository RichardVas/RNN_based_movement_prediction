import numpy as np
import matplotlib.pyplot as plt

from grapher import *

#from lstm1119 import *

test1 = np.array([
    [0, 0],
    [-1, 0],
    [-2, 0],
    [-3, 0],
    [-4, 0]
])

test2 = np.array([
    [0, 0],
    [0, 2],
    [0, 4],
    [0, 6],
    [0, 8],
    [0, 10],
    #   [0,12],
    #   [0,14]
])

test3 = np.array([
    [0, 0],
    [-1, -1],
    [-2, -2],
    [-3, -3],
    [-4, -4],
    [-5, -5],
    [-6, -6],
    [-7, -7]
])

test4 = np.array([
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 7],
    [8, 8],
])

test5 = np.array([
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    [0, 7],
    [0, 8],
])

test6 = np.array([
    [0, 0],
    [-1, -1],
    [-1, -1],
    [-1, -1],
    [-1, -1],
    [-1, -1],
    [-1, -1],
    [-2, -2]
])

test7 = np.array([
    [0, 0],
    [-1, 1],
    [-2, 2],
    [-3, 3],
    [-3, 4],
    [-3, 5],
    [-3, 6],
    [-3,7],
])

test8 = np.array([
    [0, 0],
    [2, 1],
    [4, 2],
    [6, 3],
    [8,4],
    [10,5],
    [12,6],



    #   [0,12],
    #   [0,14]
])

test9 = [
    [3,0],
    [5,0],
    [9,0],
    [9,0],
    [15,0],
    [18,0],
    [21,0],
    [24,0],
]


data = np.array(test9)
#data = data.reshape(-1,2)
x, y = data.T
#plt.scatter(x,y)
#plt.plot(x,y)
#plt.show()


if __name__ == "__main__":

    shower = Grapher()
    #qwe = Predictor()

    shower.addArray(test1)
    shower.addArray(test2)
    shower.addArray(test3)
    shower.addArray(test4)
    shower.addArray(test5)
    shower.addArray(test6)
    shower.addArray(test7)
    shower.addArray(test8)
    shower.addArray(test9)
    shower.displayGraph()

