import numpy as np
det = np.linalg.det
inv = np.linalg.inv

def inverse(arr):
  if round(det(arr), 2) == 0:
    return 'no inverse'
  return inv(arr)

if __name__ =='__main__':
  A = np.mat('1,2,3;4,5,6;7,8,9')
  print(inverse(A))
  A = np.mat('1,2,3;4,5,6;7,8,8')
  print(inverse(A))
