def durgeonGame(dungeon):
  minVal = [float('inf')]
  m = len(dungeon)
  n = len(dungeon[0])
  if m == 1 and n == 1:
    # print('xx')
    return abs(dungeon[0][0])+1 if dungeon[0][0] < 0 else 1


  def solve(i, j, res, maxi):
    if i == m-1 and j == n-1:
      # print(maxi, 'inside')
      if res+dungeon[i][j] <= 0:
        maxi =  max( abs(res+dungeon[i][j])+1, maxi)
      
      minVal[0] = min(minVal[0], maxi)
      return
    if i >= m or j >= n:
      return

    res += dungeon[i][j]
    # print(res, 'resss', maxi)
    if res <= 0:
      x = abs(res) + 1
      maxi = max(x, maxi)
    solve(i, j+1, res, maxi)
    solve(i+1, j, res, maxi)
  solve(0,0,0,1)
  return minVal[0]
grid = [[-2,-3,3],[-5,-10,1],[10,30,-5]]

print(durgeonGame(grid))

# what i learnt
# 1. in recursion call, backtracking one - if we use res aray then as we know it is call by reference
# then mns it gets altered diring calls thats why we put res.pop at end becasue for that call stack
# picture we have to update the res value whereas in integeer, string all all me apko
# no need to pop as wo har frame me purana h state maintain krte h so no need to pop - check allPthTraverse file

# 2. i did this question using checked every path and maintained max kita health chahye next cell pe
# visit k lie as the questn states ki u have to survice at each cell. so its imp har step me kita 
# max health chahye..i maintained that and end me har path me min kaun sa chahye but it gave me limit exceeded

# 3.there are two types of approaches that in dp problem, we can take - here normal j hme pta tha
# dp[i][j-1], dp[i-1][j] islie nhi lia because ye har path pe max health kita chahye hga wo maintain
# nhi kr payega to reach that cell.wo best health kita wo store krega which is not asked in this cell
# as in every cell, knight pahcuega h nhi if it gets dropeed to 0 or below. another explanatn bwelow - 
# 1st explanation
# The reason why we are not starting from the top is because we want the knight at all times if we 
# start at the top then we may have a point where the knight's life drops below 0 but due to the 
# orb present in the next right or down rooms the value becomes positive. It doesnt show up while
#  coding but if you print out the matrix with having the minimum health that you calculated with
#   this approach you might see there are negative values in the matrix which indicate this we need
#    to take care at all times that the prince is alive
# 2nd one
# We are trying to find minHP at [0][0]; this is the end goal. The base case occurs at [m -1][n - 1], so DP must begin there and work its way to the end goal.
#  Took me a while to realize this.
#  see below code
def dungeonGame(dungeon):

  n = len(dungeon)
  m = len(dungeon[0])
  dp = [[float('inf') for j in range(m+1)] for i in range(n+1)]
  dp[n][m - 1] = 1
  dp[n - 1][m] = 1
  for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
      need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
      dp[i][j] = 1 if need <= 0 else need
  return dp[0][0]



# other code
def dungeonGame(dungeon):
  m = len(dungeon)
  n = len(dungeon[0])
  dp = [[float('inf') for j in range(n)] for i in range(m)]
  def solve(i, j):
    if i >= m or j >= n:
      return float('inf')
    if i == m-1 and j == n-1:
      return abs(dungeon[i][j])+1 if dungeon[i][j] <= 0 else 1
    if dp[i][j] != float('inf'):
      return dp[i][j]
    right = solve(i, j+1)
    down = solve(i+1, j)
    # if we are at any particular cell we must ask should we go right or down ?
    #  if we know the answer for min health req if we go right vs we go down,
    #  then we can easily choose
    minHealth = min(down, right) - dungeon[i][j]
    # this line is interesting as its saying if positve answer meaning frst cell me kuch negative
    # tha so wo chahye hge negative point whereas if neagtive meaning koi positive num
    # hai so 1 lia
    dp[i][j] =  1 if minHealth <= 0 else minHealth 
    return dp[i][j]
    
  return solve(0, 0)
      
      
# so on below code recursiom approach plus memo
# https://leetcode.com/problems/dungeon-game/discuss/745340/post-Dedicated-to-beginners-of-DP-or-have-no-clue-how-to-start