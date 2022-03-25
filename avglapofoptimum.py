import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def slipSteerToLap():
	fastestLap = 0
	avgLap = 0
	nooflaps = 0

	df = pd.read_csv('SlipToInput/NewSlipToARB_FrontRear&FrontToe&FrontBump&Diff_Coast&Front_Rebound.csv')

	# First gather the static toe of the setup 
	for index, row in df.iterrows():
		if -1000 < row['ARB_FrontRear&FrontToe&FrontBump&Diff_Coast&Front_Rebound'] < 500:
			file = row['Output_File']
			dflap = pd.read_csv(f'copyValidLapsOutput/{file}')
			fastestlap = dflap.iloc[-1]['acsys.CS.BestLap']
			avgLap += fastestlap
			nooflaps += 1

	print(avgLap/nooflaps)
	print(nooflaps)

if __name__ == "__main__":
	slipSteerToLap()