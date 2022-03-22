def Triangle(triangle):
  n = len(triangle)
  dp = [[0 for j in range(i+1)] for i in range(n)]
  dp[0][0] = triangle[0][0]
  for i in range(1, n):
      for j in range(i+1):
          if j == 0:
              dp[i][j] = triangle[i][j] + dp[i-1][j]
          elif j >= len(triangle[i-1]):
              dp[i][j] = triangle[i][j] + dp[i-1][j-1]
          else:
              dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
  minVal = float('inf')
  for i in range(n):
      minVal = min(minVal, dp[n-1][i])
  return minVal
              