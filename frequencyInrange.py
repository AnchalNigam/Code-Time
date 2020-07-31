T = input()
def frequencyInRange(arr):
  dic = {}
  resArr = [0]*len(arr)
  for i in range(len(arr)):
    if arr[i] not in dic:
      dic[arr[i]] = 1
    else:
      dic[arr[i]] += 1
  print(dic)
  for i in dic:
    resArr[i-1] = dic[i]
  print(resArr)




for i in range(int(T)):
  k = int(input())
  arr = list(map(int,input().split()))
  frequencyInRange(arr)