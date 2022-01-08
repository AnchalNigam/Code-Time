def minPathSum(grid):
  m = len(grid)
  n = len(grid[0])
  dp = [[0 for i in range(n)] for j in range(m)] 
  for i in range(m):
    for j in range(n):
      if i == 0 and j == 0:
          dp[i][j] = grid[i][j]
      elif i == 0 and j != 0:
          dp[i][j] = grid[i][j] + dp[i][j-1]
      elif i != 0 and j == 0:
          dp[i][j] = grid[i][j] + dp[i-1][j]
      else:
          dp[i][j] = grid[i][j] + min(dp[max(i-1, 0)][j], dp[i][max(j-1, 0)])
  return dp[m-1][n-1]

# same funda, visualize fo one cell,, how to get min sum,, obvio above and left path check and who
# ever is min, consider it..like unique path. main apprach is think of smaller ip. this is top
# down approach of DP