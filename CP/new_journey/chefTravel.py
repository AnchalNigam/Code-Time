T = int(input())
result = []
def equalPairs(arr):
  dic = {}
  maxC = 0
  for num in arr:
    if num not in dic:
      dic[num] = 1
    else:
      dic[num] += 1
    maxC = max(dic[num], maxC)
  return len(arr) - maxC




for t in range(T):
  N = int(input())
  arr = list(map(int,input().split()))

  result.append(equalPairs(arr))

for res in result:
  print(res)