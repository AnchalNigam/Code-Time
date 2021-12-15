def maxSubArray(nums):
  maxSum = float('-inf')
  summation = 0
  for idx in range(len(nums)):
      summation = max(nums[idx], nums[idx]+summation)
      maxSum = max(summation, maxSum)
  return maxSum
      

# time complexity - o(n)