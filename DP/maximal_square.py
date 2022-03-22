# recursion + memo

def maximalSquare(matrix):
  n = len(matrix)
  m = len(matrix[0])
  dp = [[-1 for j in range(m)] for i in range(n)]
  def solve(i, j):
      if i > n or j > m or i < 0  or j < 0  or matrix[i][j] != "1":
          # print('what', i, j, m, n)
          return 0
      # print(dp)
      if dp[i][j] != -1:
          return dp[i][j]
      dp[i][j] =  min(solve(i, j-1), solve(i-1, j), solve(i-1, j-1)) + 1
      # print(dp[i][j])
      return dp[i][j]
  maxO = 0
  for i in range(n):
      for j in range(m):
          if(matrix[i][j] == "1"):
              res = solve(i, j)
              # print(res, i, j, 'checking')
              maxO = max(maxO, res)
              
  return pow(maxO,2)

def maximalSquare(matrix):
  n = len(matrix)
  m = len(matrix[0])
  dp = [[0 for j in range(m+1)] for i in range(n+1)]
  maxo = float('-inf')
  for i in range(1, n+1):
      for j in range(1,m+1):
          if matrix[i-1][j-1] == "1":
              # print('inside', i, j)
              dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
          maxo = max(maxo, dp[i][j])
              
  return maxo**2


  # in this problem, only main logic was dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
  # min of three+1 as any min mns uske upar me kuch 0 hga (cosnider min)