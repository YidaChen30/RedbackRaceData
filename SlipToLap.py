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
			# avgSlip += ((row['SlipAngle_FL'] - row['CamberDeg_FL']) + (row['SlipAngle_FR'] + row['CamberDeg_FR'])) - (row['SlipAngle_RL'] + row['SlipAngle_RR'])
			# avgSlip += ((row['SlipAngle_FL']) + (row['SlipAngle_FR'])) - (row['SlipAngle_RL'] + row['SlipAngle_RR'])
			avgSlip += ((row['SlipAngle_FL'] - row['CamberDeg_FL']) + (row['SlipAngle_FR'] + row['CamberDeg_FR'])) - ((row['SlipAngle_RL'] - row['CamberDeg_RL']) + (row['SlipAngle_RR'] + row['CamberDeg_RR']))


			# Finding average lap time for a setup
			# If it is a new lap, grab the lap time of the previous lap
			if row['acsys.CS.LapCount'] - 1 == prevLap:
				avgLap += row['acsys.CS.LastLap']
				totalLaps += 1
			prevLap = row['acsys.CS.LapCount']


		avgSlip = avgSlip / len(df.index)
		avgLap = avgLap / totalLaps 
		list_data = [file, avgSlip, avgLap]
		# data[0].append(file)
		# data[1].append(avgSlip)
		# data[2].append(avgLap)
		data.append(list_data)

	df_new = pd.DataFrame(data, columns = ['Output_File', 'AvgSlip', 'AvgLap'])
	# df_new.plot.scatter(x='AvgSlip', y='AvgLap')
	df_new.to_csv(f"LapToSlipPlotWithCamberFR.csv", index=False)

if __name__ == "__main__":
	slipToLap()
  


"""
data = [['','']]

for files in output:
	calculate avglaptime
	calculate avgslip
	data[0].append(avglaptime)
	data[1].append(avgslip)

dfnew = pd.DataFrame(data, columns = ['AvgLapTime', 'AvgSlip']
"""