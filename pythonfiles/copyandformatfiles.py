#Will go through all the csv files and print out the name of the one with the fastest time.
import os
import shutil

#KEEP IN MIND THIS FILE MIGHT NOT WORK IN YOUR COMPUTER AS MY FILES ARE IN MY D DRIVE
def movefiles():

  #this is to keep track of the numbers of the files
  datanum = 0

  #get the names of the files in the directory where all the csvs are stored.
  datafiles = os.listdir('data0/')

  #loop through the list of files and start moving them into one file
  for files in datafiles:

    # this is to make sure that the numbers below 10 have the 0 in front of the number.
    tempdatanum = str(datanum)

    if datanum < 10:
      tempdatanum = "0" + str(datanum)

    #copying out of their individual folders into one main folder.
    shutil.copy("data0/data0_" + tempdatanum + "/output.csv", "cardata/output" + str(datanum) + ".csv")
  
    datanum = datanum + 1

if __name__ == "__main__":
  print("current working directory is " + os.getcwd())
  movefiles()