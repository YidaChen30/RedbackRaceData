import pandas as pd
import matplotlib.pyplot as plt 

#
def generatePlots():
    df = pd.read_csv('./combineddata.csv')
    i = 17
    plt.scatter(df.iloc[:, -2] , df.iloc[:, -1])

    plt.title(f'Graph {df.columns[i]}')

    plt.ylabel(f'{df.columns[i]}')

    #plt.ylabel('fastest lap time')
    plt.xlabel('Slip Angle')

    plt.show()

if __name__ == "__main__":
  generatePlots()