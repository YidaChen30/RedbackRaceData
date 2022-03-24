import pandas as pd
import os


def RemoveInvalidLaps():
    # Gets the file names of all the files in the directory
    datafiles = os.listdir('ColsRemovedOutput/')


    for file in datafiles:

        df = pd.read_csv(f"ColsRemovedOutput/{file}")
        file_no = file[14:18]
        for index, row in df.iterrows():
            if row['acsys.CS.LastLap'] > 50000:
                currentLap = (row['acsys.CS.LapCount'])
                indexNames = df[df['acsys.CS.LapCount'] == (currentLap - 1)].index
                df.drop(indexNames, inplace = True)
        df.to_csv(f"ValidLapsOutput/VLoutput{file_no}.csv")

if __name__ == "__main__":
  RemoveInvalidLaps()