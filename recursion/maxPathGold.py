def maxPathGold(grid):
  m = len(grid)
  n = len(grid[0])
  finalMax = float('-inf')
  mGold = [float('-inf')]
  def getMaxGold(i, j, gold):

      if(i < 0 or j < 0 or i >= m or j >= n):
          return 0
      if grid[i][j] == '*' or grid[i][j] == 0:
          return 0
      curC = grid[i][j]
      gold += grid[i][j]
      grid[i][j] = '*'
      getMaxGold(i, j+1, gold)
      getMaxGold(i+1, j, gold)
      getMaxGold(i-1, j, gold)
      getMaxGold(i, j-1, gold)
      grid[i][j] = curC
      mGold[0] = max(gold, mGold[0])
      return mGold[0]

      
  for i in range(m):
      for j in range(n):
          maxx = getMaxGold(i, j, 0)
          finalMax = max(maxx, finalMax)
  return finalMax

grid = [[0,6,0],[5,8,7],[0,9,0]]

print(maxPathGold(grid))