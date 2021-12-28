def houseRobber(nums, start, end):
  n = (end - start)+1
  dp = [-1 for i in range(len(nums))]
  if n == 0:
    return 0 
  dp[start] = nums[start]
  if n == 1:
    return dp[start]
  dp[start+1] = max(nums[start],nums[start+1])
  if n == 2:
    return dp[start+1]
  
  for i in range(start+2, len(nums)):
    dp[i] = max(dp[i-2]+nums[i], dp[i-1])
  return dp[end]

def houseRobberII(nums):
  n = len(nums)
  if(len(nums) == 1):
    return nums[0]
  return max(houseRobber(nums, 0, n-2), houseRobber(nums, 1, n-1))
nums = [1]
print(houseRobberII(nums))


# in this as circular house, it means either we can loot first or last,, so broke down the prob
# first 0 to n-2 dekha then 1 to last wale k include krke dekha.which one is max is ans
  
