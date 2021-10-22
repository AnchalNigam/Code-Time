def maxRobber(nums):
  dp = [-1 for idx in range(len(nums))]
  def solve(n):
      if n < 0:
          return 0
      if dp[n] != -1:
          return dp[n]
      dp[n] = max(solve(n-1), nums[n]+solve(n-2))
      return dp[n]
      
  solve(len(nums)-1)
  maximum = float('-inf')
  for idx in range(len(dp)):
      maximum = max(dp[idx], maximum)
  return maximum
            
# here the approach is like max robbery krne the. here the scene is u cant choose each eleent
# like in knapsach weight baag is constraint and here adjacent one was constraint
# here i appoached this issue by thinking of smaller input. smaller then goes further