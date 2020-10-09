T = int(input())
replaceForXStatus = []
# 12 3 4 2
def replaceForX(x,p,k,arr):
  # arr.sort()
  # if x not in arr:
  #   if p == k:
  #     return 0
  #   return -1
  # else:
  #   if arr[p-1] == x:
  #     return 0
  #   else:
  #     for idx in range(len(arr)):
  #       if arr[idx] == x:
  #         xIdx = idx
  #         break
  #     if p > k or idx+1>k:
  #       return -1
  #     else:
  #       return abs(xIdx+1-p)
  arr.sort()
  if x not in arr:
    if p == k:
      return 1
    return -1
  else:
    if arr[p-1] == x:
      return 0
    if p == k:
      return 0
    else:
      for idx in range(len(arr)):
        if arr[idx] == x:
          xIdx = idx
          break
      
      if idx+1 > k > p or p > k > idx+1:
        return -1
      return abs(xIdx+1-p)

      
  





for t in range(T):
  replaceForXData = list(map(int,input().split()))
  replaceForXArr = list(map(int,input().split()))
  replaceForXStatus.append(replaceForX(replaceForXData[1], replaceForXData[2], replaceForXData[3], replaceForXArr))

for result in replaceForXStatus:
  print(result)

