def subset_sum(arr, sum):
  dp = [[-1 for idx in range(sum+1)] for idx2 in range(len(arr)+1)]
  for i in range(len(arr)+1):
    for j in range(sum+1):
      if i == 0:
        dp[i][j] = 0
      if j == 0:
        dp[i][j] = 1
  for i in range(1, len(arr)+1):
    for j in range(1, sum+1):
      if arr[i-1] <= j:
        dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
      else:
         dp[i][j] = dp[i-1][j]
  return dp
arr = [1,1,2,3]
print(subset_sum(arr, 4))