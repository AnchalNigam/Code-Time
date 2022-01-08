def uniquePaths(obstacleGrid):
  m = len(obstacleGrid)
  n = len(obstacleGrid[0])
  
  dp = [[0 for i in range(n)] for j in range(m)]
  if obstacleGrid[0][0] != 1:
      dp[0][0] = 1
  for i in range(m):
    for j in range(n):
      if obstacleGrid[max(i-1, 0)][j] == 1 and obstacleGrid[i][max(j-1, 0)] != 1:
        dp[i][j] = dp[i][max(j-1, 0)]
      elif obstacleGrid[i][max(j-1, 0)] == 1 and obstacleGrid[max(i-1, 0)][j] != 1 :
        dp[i][j] = dp[max(i-1, 0)][j]              
      elif obstacleGrid[i][j] != 1 and obstacleGrid[max(i-1, 0)][j] != 1 and obstacleGrid[i][max(j-1, 0)] != 1:     
        if (i != 0 or j != 0) :
          dp[i][j] = dp[max(i-1, 0)][j] + dp[i][max(j-1, 0)]
  if(obstacleGrid[m-1][n-1]) == 1:
    return 0
  return dp[m-1][n-1]

