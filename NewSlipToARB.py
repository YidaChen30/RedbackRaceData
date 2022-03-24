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

		# Multiplying front ARB and rear ARB with diff_coast
		# dataIn.append((dfIn.iloc[7]['value'] / dfIn.iloc[8]['value']) * dfIn.iloc[3]['value'])
		
		# Dividing front ARB with rear ARB
		# dataIn.append(dfIn.iloc[7]['value'] / dfIn.iloc[8]['value'])

		# Tyre Pressure with Slip
		# dataIn.append(dfIn.iloc[31]['value'] / dfIn.iloc[32]['value'])

		# Rebound to Slip -> Low should be understeer
		# dataIn.append(dfIn.iloc[18]['value'])

		# Rear_ARB
		dataIn.append(dfIn.iloc[3]['value'])


	df_new['Diff_Coast'] = dataIn
	df_new.to_csv(f"NewSlipToDiff_Coast.csv", index=False)

if __name__ == "__main__":
	SlipToARB()