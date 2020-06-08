# 4 4
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

T = input()
def spiralMatrix(arr, row, column):
  k = l = 0
  while k < column and l < row:
    for i in range(column):
      print(arr[l][k])
      k += 1
    l += 1
    for i in range(row):
      print(arr[l][k])
      l += 1
    k -= 1
    for i in range(column):
      print(arr[l][k])
      k -= 1
    
    for i in range(row-1):
      print(arr[l][k])
      l -= 1
    k += 1
    
  




for i in range(int(T)):
  row,column = input().split()
  arr = input().split()
  print(spiralMatrix(arr, int(row), int(column)))