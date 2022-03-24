from matplotlib.pyplot import axis
import pandas as pd
import os 
import numpy as np


dfColumns = ['File Name', 
  'brakes_DATA_MAX_TORQUE', 
  'brakes_DATA_FRONT_SHARE',	
  'drivetrain_DIFFERENTIAL_POWER',
  'drivetrain_DIFFERENTIAL_COAST',	
  'drivetrain_DIFFERENTIAL_PRELOAD',	
  'suspensions_BASIC_WHEELBASE', 
  'suspensions_BASIC_CG_LOCATION',	
  'suspensions_ARB_FRONT',
  'suspensions_ARB_REAR',	
  'suspensions_FRONT_TRACK',	
  'suspensions_FRONT_ROD_LENGTH', 
  'suspensions_FRONT_TOE_OUT',	
  'suspensions_FRONT_STATIC_CAMBER',	
  'suspensions_FRONT_SPRING_RATE',	
  'suspensions_FRONT_BUMP_STOP_RATE',	
  'suspensions_FRONT_PACKER_RANGE',	
  'suspensions_FRONT_DAMP_BUMP', 
  'suspensions_FRONT_DAMP_FAST_BUMP',	
  'suspensions_FRONT_DAMP_REBOUND',	
  'suspensions_FRONT_DAMP_FAST_REBOUND',	
  'suspensions_REAR_TRACK',	
  'suspensions_REAR_ROD_LENGTH',	
  'suspensions_REAR_TOE_OUT',	
  'suspensions_REAR_STATIC_CAMBER',	
  'suspensions_REAR_SPRING_RATE',	
  'suspensions_REAR_BUMP_STOP_RATE',	
  'suspensions_REAR_PACKER_RANGE',	
  "suspensions_REAR_DAMP_BUMP",	
  'suspensions_REAR_DAMP_FAST_BUMP',
  'suspensions_REAR_DAMP_REBOUND',	
  'suspensions_REAR_DAMP_FAST_REBOUND',
  'tyres_FRONT_PRESSURE_STATIC',
  'tyres_REAR_PRESSURE_STATIC',
  'SlipAngle_FR',
  'Fastest Lap']

def createDataframe():
  cardatanames = os.listdir('../cardata')

  inputdatanames = os.listdir('../carinputdata')

  combinedDf = pd.DataFrame(columns= dfColumns, index=['File Name'])

  #get rid of the first line because for some reason dataframe is created with an empty row
  combinedDf = combinedDf.iloc[1:]

  # loop through 2 arrays at once wtf
  for (outnames, innames) in zip(cardatanames, inputdatanames):
    df = pd.read_csv( f'../cardata/{outnames}')

    df1 = pd.read_csv( f'../carinputdata/{innames}')

    # start of the row which will be appended
    name = [innames]

    #transpose the vertical values of the input file to horizontal
    values =  df1.transpose().iloc[1].to_list()

    print(values)
    # add in average slip angle
    #print(type(df['SlipAngle_FR'].abs().mean()))
    values.append(df['SlipAngle_FR'].abs().mean())

    
    #combine name of file and input values
    rowData = np.concatenate((name, values))

    #combine the other stuff with best lap time
    rowData = np.append(rowData, [df.iloc[-1,5]])
    
    #print(combinedDf)

    # turn that array into dataframe
    rowData = pd.DataFrame(data=[rowData], columns= dfColumns)
    #print(rowData)
    
    #rowData.to_csv('./test2.csv', index=False)
    
    combinedDf = pd.concat([combinedDf, rowData])

  combinedDf.to_csv('./combineddata.csv', index=0)

if __name__ == "__main__":
  createDataframe()