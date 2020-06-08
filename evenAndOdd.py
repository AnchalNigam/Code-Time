T = input()
def evenAndOdd(arr):
  evenArr = []
  oddArr = []
  for i in range(len(arr)):
    if arr[i]%2 == 0:
      evenArr.append(arr[i])
    else:
      oddArr.append(arr[i])
  
  evenArr.sort()
  oddArr.sort()
  evenArr.extend(oddArr)
  print(evenArr)



for i in range(int(T)):
  sizeArr = input()
  arr = list(map(int,input().split()))
  print(evenAndOdd(arr))