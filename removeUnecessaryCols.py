import pandas as pd
import os

def RemoveUnecessaryCols():
    # Gets the file names of all the files in the directory
    datafiles = os.listdir('cardata/')

    for file in datafiles:

        df = pd.read_csv(f"cardata/{file}")
        file_no = file[6:10]
        df = df[['acsys.CS.SpeedKMH', 'acsys.CS.Gas', 'acsys.CS.Brake', 'acsys.CS.BestLap', 'acsys.CS.LapCount', 'acsys.CS.LapTime', 'acsys.CS.LastLap', 'acsys.CS.Steer', 'WorldPosition_X', 'WorldPosition_Y', 'WorldPosition_Z', 'CamberDeg_FR', 'CamberDeg_FL', 'CamberDeg_RL', 'CamberDeg_RR', 'SlipAngle_FL', 'SlipAngle_FR', 'SlipAngle_RL', 'SlipAngle_RR', 'CurrentTyresCoreTemp_FL', 'CurrentTyresCoreTemp_FR', 'CurrentTyresCoreTemp_RL', 'CurrentTyresCoreTemp_RR', 'acsys.CS.ToeInDeg']]
        df.to_csv(f"ColsRemovedOutput/ModifiedOutput{file_no}.csv", index=False)


if __name__ == "__main__":
  RemoveUnecessaryCols()