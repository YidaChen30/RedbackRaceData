import os
import shutil
  
def move():
  for x in range (0, 51):
    num = str(x)
    if x < 10:
      num = "0" + str(x)
    shutil.copy(f'moredata/data0/data0_{num}/input_params.csv', f'cardata/input/input_params0_{num}.csv')

  for x in range(0, 33):
    num = str(x)
    if x < 10:
      num = "0" + str(x)

    shutil.copy(f'moredata/data1/data1_{num}/input_params.csv', f'cardata/input/input_params1_{num}.csv')
  
  for x in range(0, 51):
    num = str(x)
    if x < 10:
      num = "0" + str(x)

    shutil.copy(f'moredata/data2/data2_{num}/input_params.csv', f'cardata/input/input_params2_{num}.csv') 
if __name__ == "__main__":
  move()