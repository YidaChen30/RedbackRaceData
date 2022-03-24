import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def slipSteerToLap():
	data = []
	datafiles = os.listdir('copyValidLapsOutput/')

	for file in datafiles:
		df = pd.read_csv(f'copyValidLapsOutput/{file}')
		totalLaps = 0
		totalRows = 0
		prevLap = 999
		avgLap = 0
		avgSlip = 0

		# First gather the static toe of the setup 
		for index, row in df.iterrows():
			if abs(row['acsys.CS.Steer']) < 0.65:
				setup_toe = row['acsys.CS.ToeInDeg']
				break


		for index, row in df.iterrows():
			# Finding average slip for a setup
			if (row['SlipAngle_FL'] + setup_toe) > row['SlipAngle_RL']:
				totalRows += 1
				avgSlip += abs(row['SlipAngle_FL'] + setup_toe)
			# Finding average lap time for a setup
			# If it is a new lap, grab the lap time of the previous lap
			if row['acsys.CS.LapCount'] - 1 == prevLap:
				avgLap += row['acsys.CS.LastLap']
				totalLaps += 1
			prevLap = row['acsys.CS.LapCount']

		if (totalRows == 0): 
			continue
		avgSlip = avgSlip / totalRows
		avgLap = avgLap / totalLaps 
		list_data = [file, avgSlip, avgLap]
		data.append(list_data)

	df_new = pd.DataFrame(data, columns = ['Output_File', 'AvgSlip', 'AvgLap'])
	# df_new.plot.scatter(x='AvgSlip', y='AvgLap')
	df_new.to_csv(f"LTSStaticToeUndersteer.csv", index=False)

if __name__ == "__main__":
	slipSteerToLap()