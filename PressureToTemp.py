import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def pressureToTemp():
	dataOut = []
	dataIn = []
	datafilesOut = os.listdir('copyValidLapsOutput/')
	datafilesIn = os.listdir('copyValidLapsInput/')

	for fileOut in datafilesOut:
		dfOut = pd.read_csv(f'copyValidLapsOutput/{fileOut}')
		avgTemp = 0
		for index, row in dfOut.iterrows():
			avgTemp += (row['CurrentTyresCoreTemp_RL'] + row['CurrentTyresCoreTemp_RR']) / 2
		
		avgTemp = avgTemp / len(dfOut.index)
		list_data = [fileOut, avgTemp]
		dataOut.append(list_data)

	df_new = pd.DataFrame(dataOut, columns = ['Output_File', 'AvgTempRear'])

	for fileIn in datafilesIn:
		dfIn = pd.read_csv(f'copyValidLapsInput/{fileIn}')
		dataIn.append(dfIn.iloc[32]['value'])

	df_new['Rear_Pressure'] = dataIn
	df_new.to_csv(f"PressureToTempRear.csv", index=False)

if __name__ == "__main__":
	pressureToTemp()