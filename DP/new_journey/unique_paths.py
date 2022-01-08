def uniquePaths(m, n):
  dp = [[0 for i in range(n)] for j in range(m)]
  for i in range(m):
    for j in range(n):
      if i == 0 or j == 0:
        dp[i][j] = 1
  for i in range(1, m):
    for j in range(1, n):
      dp[i][j] = dp[i-1][j] + dp[i][j-1]

  return dp[m-1][n-1]


# main focus is here to react at specific cell, if we know how diagonals value then we can 
# find that current cell by adding it as down and right steps are possible..so i, j-1 and i-1,j
# values are imp 
# space is o(m*n)

class Solution:
    def uniquePaths(self, m, n):
        dp = [1]*n
        for _, j in product(range(1, m), range(1, n)):
            dp[j] += dp[j-1]
        return dp[-1]
# Time Complexity : O(m*n), for computing dp values for each of the m*n cells.
# Space Complexity : O(n), required to maintain dp. We are only keeping two rows of length n giving space complexity of O(n).
