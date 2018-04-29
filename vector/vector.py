import numpy as np

def orthify(A):			#斯密特正交化
  B = np.zeros_like(A,dtype='float')
  count = 0
  for a in A.T:			#get the column
    a = a.T			#change it to column vector
    br = np.copy(a)
    for i in range(0,count):
      b = B[:,i]
      br = br - (b.T).dot(a)[0,0]/((b.T).dot(b)[0,0])*b
    B[:,count] = br
    count = count + 1
   #以上完成正交，接下来进行单位化
  for i in range(B.shape[1]):
    b = B[:,i]
    b = b/np.linalg.norm(b)
    B[:,i] = b
  return B

def get_vector_angle(a,b):
  cos_angle = a.T.dot(b)[0][0]/(np.linalg.norm(a)*np.linalg.norm(b)) 
  angle = np.arccos(cos_angle)
  angle2 = angle*360/2/np.pi
  return angle, angle2

if __name__=='__main__':
  a = np.mat('1;2;3')
  b = np.mat('2;4;9')
  angles = get_vector_angle(a,b)
  print(angles)

  A = np.mat('1,0,-2;1,4,1;-1,1,1')
  B = orthify(A)
  print(B)
