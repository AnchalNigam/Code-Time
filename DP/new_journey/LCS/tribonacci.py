def tribonacci(n):
  if n == 0:
    return 0
  elif n <= 2:
    return 1
  dp = [-1 for idx in range(n+1)]
  dp[1] = 1
  dp[2] = 1
  def solve(x):
    if x <= 0:
      return 0
    if dp[x] != -1:
      return dp[x]
    dp[x] = solve(x-1) + solve(x-2) + solve(x-3)
    return dp[x]
  return solve(n)

    
# approach 1 - memozization + recursion

def tribonacci(n):
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  dp = [-1 for idx in range(n+1)]
  dp[0] = 0
  dp[1] = 1
  dp[2] = 1
  for idx in range(3, n+1):
    dp[idx] = dp[idx-1] + dp[idx-2] + dp[idx-3]
  return dp[n]

# approach 2 - looping