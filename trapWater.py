T = input()
# 8 8 2 4 5 5 1
# 7 4 0 9
# 3 0 0 2 0 4
# def trapWater(arr):
#   totalTrappedWater = 0
#   start = 0
#   end = len(arr) - 1
#   minEndVal =  min(arr[0], arr[len(arr) - 1])
#   end -= 1
#   while start < end:
#     if arr[end] == 0:
#       totalTrappedWater += minEndVal
#     else:
#       if arr[end] < minEndVal:
#         totalTrappedWater += (minEndVal - arr[end])
#     end -= 1
#   return totalTrappedWater

# 1 1 5 2 7 6 1 4 2 3 
def trapWater(arr):
  totalTrappedWater = 0
  start = 0
  end = len(arr) - 1
  if arr[start] < arr[end]:
    minEndVal = arr[start]
    end -= 1
  else:
    minEndVal = arr[end]
    start += 1
  trappedArr = []
  while start < end:
    if minEndVal > arr[end]:
      totalTrappedWater += minEndVal - arr[end]
      # minEndVal = arr[start]
    else:
      minEndVal = arr[end]
      trappedArr.append(totalTrappedWater)
      totalTrappedWater = 0
      start +=1 
    end -= 1
      
    

  return trappedArr


for i in range(int(T)):
  sizeArr = input()
  arr = input().split()
  arr = list(map(int, arr))
  print(trapWater(arr))