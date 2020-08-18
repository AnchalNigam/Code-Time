arr = list(map(int, input().split()))
target = int(input())
arr.sort()
closeSum = arr[0]+arr[1]+arr[2]
for idx in range(len(arr)-2):
  initialSum = arr[idx]
  lPointer = idx+1
  rPointer = len(arr)-1
  while(lPointer < rPointer):
    summation = initialSum + arr[lPointer] + arr[rPointer]
    if(abs(closeSum - target) > abs(summation-target)):
      closeSum = summation
    if(summation < target):
      lPointer = lPointer + 1
    else:
      rPointer = rPointer - 1

  print(closeSum)

