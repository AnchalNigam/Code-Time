T = input()
def posAndNeg(arr):
  posArr = []
  negArr = []
  for i in range(len(arr)):
    if arr[i] >= 0:
      posArr.append(arr[i])
    else:
      negArr.append(arr[i])
  if len(posArr) > len(negArr):
    traverseLen = len(negArr)
  else:
    traverseLen = len(posArr)
  for i in range(traverseLen):
    arr[i*2] = posArr[i]
    arr[(i*2)+1] = negArr[i]
  if len(posArr) > len(negArr):
    arr[((i+1)*2):] = posArr[(i+1):]
  else:
    arr[((i+1)*2):] = negArrs[(i+1):]
  print(arr)




for i in range(int(T)):
  sizeArr = input()
  arr = list(map(int,input().split()))
  posAndNeg(arr)