#!/usr/local/bin/python3

def show_array(num):
  arrays = []			#记录所有全排列
  book = [0] * num		#用于标记每个值是否被用到
  ls = []			#记录一个排列的结果
  def get_next(step):		#采用函数编程 使用深度搜索方法
    if step > num:		#当完成一个排列时记录到arrays数组中
      arrays.append(ls[:])	#使用ls[:]能够拷贝值，而不是引用
      return  			#返回
    for i in range(1, num+1):	
      if book[i-1] == 0:	#如果i没有被使用，则将其加入ls数组
        ls.append(i)		
        book[i-1] = 1		#然后将i标记为已经用过
        get_next(step+1)	#递归调用，深度搜索，进入下一步
        ls.pop()		#返回后弹出最后加入的值
        book[i-1] = 0 		#将i标记为没有用过
  get_next(1)			#进行调用
  return arrays, len(arrays)	#返回所有排列，和数组的长度，即排列的个数
     
def get_sign(arr):		#获得逆序值
  if not isinstance(arr, list):	#判断输入是否为一个数组
    print('wrong input')	
    return
  start = 0			#计算方法采用遍历 start表示起点 待比较数值
  count = 0			#记录逆序值
  while start < len(arr) - 1:	#待比较的值从0到-2
    for i in arr[start+1:]:	#与后面的值一一比较
      if arr[start] > i:	
        count = count + 1	
    start = start + 1		#对下一个值进行比较
  return count			

if __name__ == '__main__':
  result = show_array(5)
  print(result)
  get_sign(1)
  print(get_sign([5,4,3,2,1]))
  
