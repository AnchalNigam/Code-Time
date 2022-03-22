def perfectSquare(n):
  nums = 1
  counter = 1
  perfectSq = []
  while nums <= n:
      perfectSq.append(nums)
      counter += 1    
      nums = counter*counter
  minVal = [float('inf')]
  def solve(i, res, target): 
      if target == 0:
          l = len(res)
          minVal[0] = min(minVal[0], l)
          return 
      if i >= len(perfectSq):
          return
      # print(res)
      if perfectSq[i] <= target:
          res.append(perfectSq[i])
          solve(i, res, target-perfectSq[i])
          res.pop()
      solve(i+1, res, target)
  solve(0, [], n)
  return minVal[0]

# did this questn by own but time limit exceeded error....

def perfectSquare(n):
  nums = 1
  counter = 1
  perfectSq = []
  while nums <= n:
      perfectSq.append(nums)
      counter += 1    
      nums = counter*counter
  minVal = [float('inf')]
  def solve(i, res, target): 
      if target == 0:
          l = len(res)
          minVal[0] = min(minVal[0], l)
          return 
      if i < 0:
          return
      # print(res)
      if perfectSq[i] <= target and (len(res)+1) <= minVal[0]:
          res.append(perfectSq[i])
          solve(i, res, target-perfectSq[i])
          res.pop()
      solve(i-1, res, target)
  solve(len(perfectSq)-1, [], n)
  return minVal[0]

def perfectSquare(n):
  dp = [-1 for i in range(n+1)]
  def solve(n):
    if n <= 3:
      return n
    if(dp[n-1]) != -1:
        return dp[n]
    mini = float('inf')
    i = 1
    while i*i <= n:
        mini = min(mini, 1+ solve(n-(i*i)))
        i += 1
    dp[n] = mini
    return dp[n]
  return solve(n)


# check how much depth and width of tree is ..depth is till n as 1 ek perfetc square hta h
# and ye 12 times neche tak ajeag h jayega ..and width square root us number k kite h 
# like in case of 12 [1,4,9] so sqrt(n)^n is complexty

# The time complexity of brute recursion is sqrt(n) ^ (n-1) ~ O( sqrt(n) ^ n ). 
# to find the quick time complexity of such recursions 
# we need to find the maximum depth and maximum width of the recursive tree. 
# Time complexity than will be width ^ depth. Thanks
import math
def perfectSquare(n):
  if n <= 3:
    return n
  dp = [float('inf') for i in range(n+1)]
  dp[0] = 0
  dp[1] = 1
  dp[2] = 2
  dp[3] = 3
  for i in range(4, n+1):
      for j in range(1, int(math.floor(math.sqrt(i))) + 1):
          # print(i-(j*j), i, j)
          dp[i] = min(dp[i], 1 + dp[i-(j*j)])
          j += 1

  return dp[n]

# this is bottom up - n*sqrt(n)
