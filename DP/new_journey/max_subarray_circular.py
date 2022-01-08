def maxSubArray(nums):
    maxSum = float('-inf')
    summation = 0
    n = len(nums)
    if n == 1:
        return nums[0]
    for pivot in range(n):
        summation = 0
        for i in range(pivot+1, n+pivot+1):
            summation = max(nums[i%n], nums[i%n]+summation)
            maxSum = max(summation, maxSum)
    return maxSum

# above approach is i took to see as pivot and from pivot+1 to pivot, kadanes algo apply but 
# time complexity is o(n2) 
    
def maxSubArrayCircular(nums):
  minSum = float('inf')
  minSummation = 0
  maxSummation = 0
  totalSum = 0
  maxSum = float('-inf')
  for idx in range(len(nums)):
    minSummation = min(nums[idx], nums[idx]+minSummation)
    minSum = min(minSummation, minSum)
    totalSum += nums[idx]
    maxSummation = max(nums[idx], nums[idx]+maxSummation)
    maxSum = max(maxSummation, maxSum)
    
  diff = totalSum-minSum
  return maxSum if diff == 0 else max(maxSum, totalSum-minSum)

  # here main approach is totalsum-minsum
  # First find the maximum subarray sum in the straight array without considering circular behaviour.
# to find the maximum circular subarray sum first find the minimum subarray sum of the array without considering circular behaviour.
# maximum circular subarray sum will be equal to total sum - minimum subarray sum of the array.
# Now the ans is maximum of maximum subarray sum and maximum subarray sum in circular behaviour
# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/633401/Kadane-Algorithm-Trick-beats-100-Java-Explained
# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/635487/Python-Kadane's-solution