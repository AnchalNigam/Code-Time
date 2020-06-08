# T = input()
def subArraySumToK(arr, k):
  dic = {}
  current_sum = 0
  result = []
  for idx,value in enumerate(arr):
    current_sum += value
    if current_sum == k:
      result.append((0,idx))
    if (current_sum-k) in dic:
      result.appaend((dic[current_sum-k]+1,idx))

    dic[current_sum] = idx
  return result


# for i in range(int(T)):
  # k = int(input())
  # arr = list(map(int,input().split()))
print(subArraySumToK([10, 2, -2, -20, 10], -10))