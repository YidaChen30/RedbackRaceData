import pandas as pd
import os


def maxToe():

	datafilesIn = os.listdir('copyValidLapsInput/')
	max_tyre_pressure = 0
	for fileIn in datafilesIn:
		dfIn = pd.read_csv(f'copyValidLapsInput/{fileIn}')
		if (dfIn.iloc[3]['value'] > max_tyre_pressure):
			max_tyre_pressure = dfIn.iloc[3]['value']

	print(f"min diff_coast is {max_tyre_pressure}")


if __name__ == "__main__":
	maxToe()