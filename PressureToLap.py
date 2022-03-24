import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def pressureToLap():
	dataOut = []
	dataIn = []
	datafilesOut = os.listdir('copyValidLapsOutput/')
	datafilesIn = os.listdir('copyValidLapsInput/')

	for fileOut in datafilesOut:
		dfOut = pd.read_csv(f'copyValidLapsOutput/{fileOut}')
		totalLaps = 0
		prevLap = 999
		avgLap = 0
		avgTemp = 0
		for index, row in dfOut.iterrows():
			if row['acsys.CS.LapCount'] - 1 == prevLap:
				avgLap += row['acsys.CS.LastLap']
				totalLaps += 1
			prevLap = row['acsys.CS.LapCount']
		
		avgTemp = avgTemp / len(dfOut.index)
		avgLap = avgLap / totalLaps 
		list_data = [fileOut, avgLap]
		dataOut.append(list_data)

	df_new = pd.DataFrame(dataOut, columns = ['Output_File', 'AvgLapTime'])

	for fileIn in datafilesIn:
		dfIn = pd.read_csv(f'copyValidLapsInput/{fileIn}')
		dataIn.append(dfIn.iloc[32]['value'])

	df_new['Rear_Pressure'] = dataIn
	df_new.to_csv(f"RearPressureToLap.csv", index=False)

if __name__ == "__main__":
	pressureToLap()