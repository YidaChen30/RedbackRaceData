import os
import matplotlib.pyplot as plt
import pandas as pd


# this is for toe, in out.
def compareInput():


  cardatanames = os.listdir('../cardata')

  inputdatanames = os.listdir('../carinputdata')

  outputarray = []
  inputarray = []

  for (outnames, innames) in zip(cardatanames, inputdatanames):

    print('reading output ' + outnames)
    print('reading input ' + innames)
    df = pd.read_csv( f'../cardata/{outnames}')

    df1 = pd.read_csv( f'../carinputdata/{innames}')

    outputarray.append(df.iloc[-1,5])
    inputarray.append(df1.iloc[2,1])

  plt.xlabel('toe degree')
  plt.ylabel('time')
  plt.scatter(inputarray, outputarray)
  plt.show()
 
if __name__ == "__main__":
  compareInput()