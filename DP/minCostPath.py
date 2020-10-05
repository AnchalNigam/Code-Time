grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
# grid = [
#   [1,3],
#   [1,5]
# ]
# grid = [[1]]
dp = [[-1 for idx in range(len(grid[0]))] for idx in range(len(grid))]
dp[0][0] = grid[0][0]
for idx in range(1, len(grid)):
    dp[idx][0] = grid[idx][0] + dp[idx-1][0]
for idx in range(1, len(grid[0])):
  dp[0][idx] = grid[0][idx] + dp[0][idx-1]
print(dp, 'check')
def getMinSum(x,y):
    if x < 0 or y < 0:
        return 0
    print(x-1, y, dp[x-1][y],dp[-1][0])
    print(x, y)
    if dp[x][y] != -1:
      return dp[x][y]
    if dp[x-1][y] == -1:
        dp[x-1][y] = getMinSum(x-1, y)
    if dp[x][y-1] == -1:
        dp[x][y-1] = getMinSum(x, y-1)
    return min(dp[x-1][y], dp[x][y-1]) + grid[x][y]
print(dp)
print(getMinSum(len(grid)-1, len(grid[0])-1))
