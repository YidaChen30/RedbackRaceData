import os
import shutil

def moveInputFiles():

  inputfoldernames0 = os.listdir('../moredata/data0')

  num = 0
  for folders in inputfoldernames0:
    temp = str(num)
    if num < 10:
      temp = "0" + temp

    shutil.copy(f'../moredata/data0/{folders}/input_params.csv', f'../carinputdata/input0_{temp}.csv')
    num += 1

  inputfoldernames0 = os.listdir('../moredata/data1')

  num = 0
  for folders in inputfoldernames0:
    temp = str(num)
    if num < 10:
      temp = "0" + temp

    shutil.copy(f'../moredata/data1/{folders}/input_params.csv', f'../carinputdata/input1_{temp}.csv')
    num += 1

  inputfoldernames0 = os.listdir('../moredata/data2')

  num = 0
  for folders in inputfoldernames0:
    temp = str(num)
    if num < 10:
      temp = "0" + temp

    shutil.copy(f'../moredata/data2/{folders}/input_params.csv', f'../carinputdata/input2_{temp}.csv')
    num += 1

  
if __name__ == "__main__":
  moveInputFiles()