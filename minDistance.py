T = input()
def minDistance(arr, x, y):
  minDis = float('inf')
  startPoint = -1
  startNum = 0 
  for i in range(len(arr)):
    if startPoint == -1 and (arr[i] == x or arr[i] == y):
      startPoint = i
      startNum = arr[i]

    elif((startPoint != -1) and ((arr[i] == x or arr[i] == y) and (startNum != arr[i])) and (abs(i-startPoint) < minDis)):
      minDis = abs(i-startPoint)
    elif(((arr[i] == x or arr[i] == y) and (startNum == arr[i]))):
      startPoint = i
  if minDis == float('inf'):
    return -1
  return minDis

for i in range(int(T)):
  sizeArr = input()
  arr = list(map(int,input().split()))
  xy = list(map(int, input().split()))
  print(minDistance(arr,xy[0],xy[1]))