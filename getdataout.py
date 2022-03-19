import os
import shutil
  
def move():
  for x in range (0, 50):
    num = str(x)
    if x < 10:
      num = "0" + str(x)
    shutil.copy(f'moredata/data0/data0_{num}/input_params.csv', f'ValidLapsInput/VLinput0_{num}.csv')

  for x in range(0, 32):
    num = str(x)
    if x < 10:
      num = "0" + str(x)

    shutil.copy(f'moredata/data1/data1_{num}/input_params.csv', f'ValidLapsInput/VLinput1_{num}.csv')
  
  for x in range(0, 50):
    num = str(x)
    if x < 10:
      num = "0" + str(x)

    shutil.copy(f'moredata/data2/data2_{num}/input_params.csv', f'ValidLapsInput/VLinput2_{num}.csv') 
if __name__ == "__main__":
  move()
  