from matplotlib.pyplot import axis
import pandas as pd
import os 
import numpy as np

def createDataframe():
  cardatanames = os.listdir('../cardata')

  inputdatanames = os.listdir('../carinputdata')


  combinedDf = pd.DataFrame(columns=['File Name', 
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
  'Fastest Lap'])

  for (outnames, innames) in zip(cardatanames, inputdatanames):
    df = pd.read_csv( f'../cardata/{outnames}')

    df1 = pd.read_csv( f'../carinputdata/{innames}')

    name = [innames]
    values =  df1.transpose().iloc[1].to_list()
    #test = np.concatenate((name, values))

    rowData = np.concatenate((name, values))

    rowData = np.append(rowData, [df.iloc[-1,5]])
    
    print(rowData)
    combinedDf = pd.concat([combinedDf, pd.Series(rowData)], axis=0)
    break

  combinedDf.to_csv('./test.csv', index=False)

if __name__ == "__main__":
  createDataframe()