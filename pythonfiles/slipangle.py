import pandas as pd
import os
import matplotlib.pyplot as plt

def slipAndTime():
  
  filenames = os.listdir('./cardata')
  concatdf = pd.DataFrame(columns=['lap time', 'average slip'])
  for files in filenames:

    df = pd.read_csv('./cardata/' + files)
    #front right slip angle average of absolute values
    frslipavg = df['SlipAngle_FR'].abs().mean()

    #best lap time

    tempdf = pd.DataFrame({'lap time': [df['acsys.CS.BestLap'].iloc[-1]], 'average slip':[ frslipavg]})

    concatdf = pd.concat([concatdf,tempdf], ignore_index= True)

  concatdf.sort_values(by=['lap time'], ascending=True)
  plt.title('slip angle against time')
  plt.xlabel('time in milliseconds')
  plt.ylabel('average absolute slip angle in radians')
  concatdf.to_csv('./slipangle.csv', index= False)


def showGraph():
  df = pd.read_csv('./slipangle.csv')
  df.sort_values(by=['average slip'], ascending=True)
  df.columns=['index', 'slip angle', 'lap time']
  print(df)

  df = df.drop(df[df['lap time'] > 45000].index)
  plt.title('slip angle against time')
  plt.ylabel('time in milliseconds')
  plt.xlabel('average absolute slip angle in radians')
  
  plt.scatter(df.iloc[:, 1], df.iloc[:, 2])
  plt.show()
if __name__ == "__main__":
  #slipAndTime()
  showGraph()