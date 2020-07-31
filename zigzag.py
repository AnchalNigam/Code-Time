T = input()
# 3 4 7 8 6 2 1
def zigzagArr(arr):
  count = 0
  for i in range(1,len(arr)):
    if arr[i] < arr[i-1] and count != 1:
      temp = arr[i-1]
      arr[i-1] = arr[i]
      arr[i] = temp

    if arr[i] > arr[i-1] and count == 1:
      temp = arr[i-1]
      arr[i-1] = arr[i]
      arr[i] = temp
    count +=1
    if count == 2:
      count = 0
  return ' '.join(map(str,arr))

for i in range(int(T)):
  sizeArr = input()
  arr = list(map(int,input().split()))
  print(zigzagArr(arr))