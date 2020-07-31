T = input()
def sortArr(arr):
  return arr[::-1]

for i in range(int(T)):
  sizeArr = input()
  arr = input().split()
  print(sortArr(arr))