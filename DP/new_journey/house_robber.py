# def houseRobber(nums):
#   n = len(nums)
#   if n == 0:
#     return 0 
#   val1 = nums[0]
#   if n == 1:
#     return val1
#   val2 = max(nums[0],nums[1])
#   if n == 2:
#     return val2
#   for i in range(2, len(nums)):
#     max_val = max(val1+nums[i], val2)
#     val1 = val2
#     val2 = max_val
#   return max_val

# here val1 is for excluding current and val2 is after incldung like at nums[i]=8 when we include 
# that elem..its is 15 which is val2 and val1 is 10 which is excluding 8 elem

def houseRobber(nums):
  n = len(nums)
  dp = [-1 for i in range(n)]
  if n == 0:
    return 0 
  dp[0] = nums[0]
  if n == 1:
    return dp[0]
  dp[1] = max(nums[0],nums[1])
  if n == 2:
    return dp[1]
  for i in range(2, len(nums)):
    dp[i] = max(dp[i-2]+nums[i], dp[i-1])
  return dp[n-1]

nums = [6, 7, 1, 3, 8, 2, 4]
print(houseRobber(nums))
  
