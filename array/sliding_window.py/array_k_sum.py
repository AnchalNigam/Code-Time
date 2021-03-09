# Given an array of integers of size ‘n’.
# Our aim is to calculate the maximum sum of ‘k’ 
# consecutive elements in the array.
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
# j = 0, 1, 2, 3, 4
# i = 1
# 16
# 17
summation = 100, 300, 200, 500, 300, 700
maxSummation = 300, 500
def maxSum(arr, k):
  i = 0
  j = 0
  maxSummation = float('-inf')
  summation = 0
  while j < len(arr):
    summation += arr[j]
    if (j-i) + 1 == k:
      print(summation, maxSummation, 'test')
      maxSummation = max(maxSummation, summation)
      summation -= arr[i]
      i += 1
    j +=  1
  return maxSummation
print(maxSum(arr, 4))
