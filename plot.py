import pandas as pd
import matplotlib.pyplot as plt 


def generatePlots():
  df = pd.read_csv('./combineddata.csv')

  for i in range(1,34):
    print(df.iloc[:, i])

    plt.scatter(df.iloc[:, -2] , df.iloc[:, i])

    plt.title(f'Graph {df.columns[i]}')

    plt.ylabel(f'{df.columns[i]}')

    #plt.ylabel('fastest lap time')
    plt.xlabel('Slip Angle FR')

    plt.show()

if __name__ == "__main__":
  generatePlots()