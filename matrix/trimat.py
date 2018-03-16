#!/usr/local/bin/python3
import numpy as np

#define the position of triangle
LEFTUP = 1			#左上三角矩阵
LEFTDOWN =2			#左下三角矩阵
RIGHTUP =3
RIGHTDOWN = 4
SLASH = 5			#反对角矩阵
ESCAPE = 6 			#正对角矩阵

#建立与筛选函数的对应关系
condition = {LEFTUP:lambda i,j,size: True if i+j<size else False, 
             RIGHTDOWN:lambda i,j,size: True if i+j >= size - 1 else False,
             LEFTDOWN:lambda i,j,size: True if i >= j else False,
             RIGHTUP:lambda i,j,size: True if i <= j else False,
             SLASH:lambda i,j,size: True if i + j == size - 1 else False,
             ESCAPE:lambda i,j,size: True if i == j else False }

#get arrays of tuples of the postion 
#that can be filled with non-zero value.
def filt(size, pos):
  nonzeros = []
  for i in range(size):
    for j in range(size):
      if condition[pos](i,j,size): 
        nonzeros.append((i,j))
  return nonzeros
  
#generate a trianglematrix of different types
def trimatrix(size, pos, *args, dtype=float, order='C'):
  template = np.zeros((size,size), dtype, order)	#建立一个全是0的方阵
  gaps = filt(size,pos) 				#筛选需要填充的位置
  times = min(len(args),len(gaps))			#找出位置数和参数个数的较小值
  for time in range(times):				
    x,y = gaps[time]					#进行赋值
    template[x][y] = args[time]
  return template
    
#get how many maxium numbers you need
#to fill the rest part of the matrix
def get_arg_num(size):
  return size*(size-1)/2

if __name__ == '__main__':
  nums = [1,4,3,5,6,6,7,8,8,9,11,12,14,15,16]
  arr1 = trimatrix(5, RIGHTUP, *nums)
  print('rightup')
  print(arr1)
  arr2 = trimatrix(3, RIGHTDOWN, *nums)
  print('rightdown')
  print(arr2)
  arr3 = trimatrix(4, LEFTUP, *nums)
  print('leftup')
  print(arr3)
  arr4 = trimatrix(5, LEFTDOWN, *nums)
  print('leftdown')
  print(arr4)
  arr5 = trimatrix(5,SLASH,*nums)
  print('slash')
  print(arr5)
  arr6 = trimatrix(4,ESCAPE,*nums)
  print('escape')
  print(arr6)
