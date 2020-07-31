T = input()
def maxFreq(arr):
  dic = {}
  for i in range(len(arr)):
      if arr[i] not in dic:
        dic[arr[i]] = 1
      else:
        dic[arr[i]] += 1
  maxFreq = max(list(dic.values()))
  minId = float('inf')
  for i in dic:
    if i < minId and dic[i] == maxFreq:
      minId = i
      
  return minId

for i in range(int(T)):
  sizeArr = input()
  arr = list(map(int,input().split()))
  print(maxFreq(arr))