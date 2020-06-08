T = input()
def subArraySumToK(arr):
  dic = {}
  current_sum = 0
  result = []
  for idx,value in enumerate(arr):
    current_sum += value
    if current_sum == 0:
      result.append((0,idx))
    if (current_sum-0) in dic:
      result.append((dic[current_sum-0]+1,idx))

    dic[current_sum] = idx
  if len(result) > 0:
    return 'Yes'
  else:
    return 'No'



for i in range(int(T)):
  k = int(input())
  arr = list(map(int,input().split()))
  print(subArraySumToK(arr))