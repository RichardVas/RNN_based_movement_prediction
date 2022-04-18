import numpy as np
from sklearn.preprocessing import MinMaxScaler
from grapher import *


# generate dataset from 0 koord
def generateSeq(seq_len):
    arr = []
    # vizszintes jobbra
    for i in range(0, seq_len + 1):
        arr.append((i, 0))
    # vizszintes balra
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, 0))
    # fuggoleges felfelé
    for i in range(0, seq_len + 1):
        arr.append((0, i))
    # fuggoleges lefele
    for i in range(0, -seq_len - 1, -1):
        arr.append((0, i))

    # diganoally +,+
    for i in range(0, seq_len + 1):
        arr.append((i, i))

    # diagonally -,-
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, i))

    # diagnoally +,-
    for i in range(0, seq_len + 1):
        arr.append((i, -i))

    # diagonally -,+
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, -i))
#incremented
#    for i in range(0, seq_len*2 + 2,2):
#        arr.append((i, 0))

#    for i in range(0, seq_len+1,1):
       #print((i*3, 0))
#        arr.append((i*3,0))

##### /2 bracket
    #diagonally -,+ / 2
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, -i/2))

    #diagonally -,+ / 2
    for i in range(0, -seq_len - 1, -1):
        arr.append((i/2, -i))

    # diganoally +,+ /2
    for i in range(0, seq_len + 1):
        arr.append((i, i/2))
        # diganoally +,+
    for i in range(0, seq_len + 1):
        arr.append((i/2, i))


        # diagonally -,- /2
    for i in range(0, -seq_len - 1, -1):
        arr.append((i, i/2))
        # diagonally -,- /2
    for i in range(0, -seq_len - 1, -1):
        arr.append((i/2, i))

    # diagnoally +,-
    for i in range(0, seq_len + 1):
        arr.append((i, -i/2))
        # diagnoally +,-
    for i in range(0, seq_len + 1):
        arr.append((i/2, -i))



# csokk
    for i in range(12,-1,-1):
        arr.append((i,0))

    return arr





app = generateSeq(12)
#print(app)


app = np.array(app)

#num_batches = 2

#print(app)



if __name__ == "__main__":
    app = np.array(generateSeq(12))
    viz = Grapher()
    viz.addArray(app)
    viz.displayGraph()

    #           (198,2)      198      2
    print(app, app.shape, len(app),len(app[0]))
    scaler = MinMaxScaler()

    dataset = scaler.fit_transform(app)
    seq_len = 13
    input_feature = 2
    dataset = dataset.reshape(-1, seq_len*input_feature)
    print(dataset)
