T = int(input())
finalIndexArr = []
def indexOfElement(arr1, arr2):
  low = 0
  high = size-1
  while low <= high:
    mid = low + (high-low)//2
    if arr1[mid] < arr2[mid]:
      high = mid-1
    elif arr1[mid] >= arr2[mid]:
      low = mid+1
  return mid

for t in range(T):
  size = int(input())
  arr1 = list(map(int, input().split()))
  arr2 = list(map(int, input().split())) 
  finalIndexArr.append(indexOfElement(arr1, arr2))

for index in finalIndexArr:
  print(index)
  
  