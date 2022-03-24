import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def SlipToARB():
	dataOut = []
	dataIn = []
	datafilesOut = os.listdir('copyValidLapsOutput/')
	datafilesIn = os.listdir('copyValidLapsInput/')

	for fileOut in datafilesOut:
		dfOut = pd.read_csv(f'copyValidLapsOutput/{fileOut}')
		avgSlip = 0

		# First gather the static toe of the setup 
		for index, row in dfOut.iterrows():
			if abs(row['acsys.CS.Steer']) < 0.65:
				setup_toe = row['acsys.CS.ToeInDeg']
				break

		for index, row in dfOut.iterrows():
			avgSlip += abs(row['SlipAngle_FL'] - setup_toe)
		
		avgSlip = avgSlip / len(dfOut.index)
		list_data = [fileOut, avgSlip]
		dataOut.append(list_data)

	df_new = pd.DataFrame(dataOut, columns = ['Output_File', 'AvgSlip'])

	for fileIn in datafilesIn:
		dfIn = pd.read_csv(f'copyValidLapsInput/{fileIn}')
		dataIn.append(dfIn.iloc[7]['value'])

	df_new['ARB_Front'] = dataIn
	df_new.to_csv(f"SlipToARB_Front.csv", index=False)

if __name__ == "__main__":
	SlipToARB()