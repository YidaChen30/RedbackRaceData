# go through all the csv files and find out the fastest lap time, can be modified to gather other data as well.

import pandas
import os

# THIS FILE ASSUMES THAT YOU HAVE FOLDER CALLED CARDATA THAT CONTAINS THE CSVS
# KEEP IN MIND THIS FILE MIGHT NOT WORK IN YOUR COMPUTER AS MY FILES ARE IN MY D DRIVE
 
def LoopAndFindFastest():

  #gets the file names of all the files in the directory
  datafiles = os.listdir('D:/projects/RedbackRaceData/cardata/')

  fastestTime = 1000000000000
  fastestFileName = ""

  for files in datafiles:

    #open a dataframe to be read with pandas
    csvdf = pandas.read_csv(f"D:/projects/RedbackRaceData/cardata/{files}")


    # gets the value of the last row in the column "acsys.CS.BestLap" which should hold the fastest lap time for the run

    if csvdf.iloc[-1, 5] < fastestTime:
      fastestTime = csvdf.iloc[-1 , 5]
      fastestFileName = files

  print("fastest time is " + str(fastestTime))
  print("filename is : " + fastestFileName)

if __name__ == "__main__":
  LoopAndFindFastest()