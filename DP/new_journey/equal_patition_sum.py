A = [1, 5, 11, 4]
def canPartition(nums):
  summation = 0 
  for idx in range(len(nums)):
    summation += nums[idx]
  if(summation % 2 != 0):
    return False
  else:
    B = summation//2
    dp = [[-1 for idx in range(B+1)]for idx in range(len(nums)+1)]
    def isSubset(A, B, n):
      if n == -1 and B == 0:
          return True
      elif n == -1 and B != 0:
          return False
      if dp[n][B] != -1:
          return dp[n][B]
      if A[n] <= B:
          dp[n][B] = isSubset(A, B-A[n], n-1) or isSubset(A, B, n-1)
          return dp[n][B]
      else:
          dp[n][B] = isSubset(A, B, n-1)
          return dp[n][B]
    return isSubset(nums, B, len(A)-1)
print(canPartition(A))

# basic logic here is if summation is odd that means no way to divide it in equal
# if even then feasible and same as subset problem, here sum would be half of total sum