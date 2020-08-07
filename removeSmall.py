T = int(input())
removeSmallArr = []
def removeSmallElem(numArr):
  numArr.sort()
  idx = 0
  while idx < len(numArr) - 1:
    if abs(numArr[idx+1]-numArr[idx]) <= 1:
      del numArr[idx]
    else:
      idx += 1
  if len(numArr) == 1:
    return 'YES'
  else:
    return 'NO'

for t in range(T):
  size = int(input())
  numArr = list(map(int, input().split()))
  removeSmallArr.append(removeSmallElem(numArr))

for result in removeSmallArr:
  print(result)