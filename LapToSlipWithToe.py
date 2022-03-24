import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def slipToLap():
	data = []
	datafiles = os.listdir('copyValidLapsOutput/')

	for file in datafiles:
		df = pd.read_csv(f'copyValidLapsOutput/{file}')
		totalLaps = 0
		prevLap = 999
		avgLap = 0
		avgSlip = 0

		for index, row in df.iterrows():
			# Finding average slip for a setup
			# avgSlip += ((row['SlipAngle_FL'] + row['acsys.CS.ToeInDeg']) + (row['SlipAngle_FR'] - row['acsys.CS.ToeInDeg'])) - (row['SlipAngle_RL'] + row['SlipAngle_RR'])
			avgSlip += (row['SlipAngle_FR'] - row['acsys.CS.ToeInDeg'])
			# Finding average lap time for a setup
			# If it is a new lap, grab the lap time of the previous lap
			if row['acsys.CS.LapCount'] - 1 == prevLap:
				avgLap += row['acsys.CS.LastLap']
				totalLaps += 1
			prevLap = row['acsys.CS.LapCount']


		avgSlip = avgSlip / len(df.index)
		avgLap = avgLap / totalLaps 
		list_data = [file, avgSlip, avgLap]
		data.append(list_data)

	df_new = pd.DataFrame(data, columns = ['Output_File', 'AvgSlip', 'AvgLap'])
	# df_new.plot.scatter(x='AvgSlip', y='AvgLap')
	df_new.to_csv(f"LTSToeFR.csv", index=False)

if __name__ == "__main__":
	slipToLap()
  