def coinChange(coins, amount):
  minVal = [float('inf')]
  def solve(i, res, target):
    if target == 0:
        minVal[0] = min(minVal[0], len(res))
        return
    if i >= len(coins):
        return
    if(coins[i] <= target):
        res.append(coins[i])
        solve(i, res, target-coins[i])
        res.pop()
    solve(i+1, res, target)
    
  solve(0, [], amount)
  if minVal[0] != float('inf'):     
      return minVal[0]
  return -1

def coinChange(amount, coins):
  dp = [float('inf') for i in range(amount+1)]
  dp[0] = 0
  for j in range(1, amount+1):
    for i in range(len(coins)):
      if coins[i] <= j:                  
        dp[j] = min(dp[j], 1 + dp[j-coins[i]])

  if(dp[amount] != float('inf')):       
    return dp[amount]
  return -1




  # dp = [[-1 for j in range(amount+1)] for i in range(len(coins)+1)]
  #       for i in range(len(coins)+1):
  #           for j in range(amount+1):
  #               if i == 0 or j == 0:
  #                   dp[i][j] = 0
  #       # print(dp)
  #       def solve(n, target):
  #           print(n, target)
  #           if target == amount:
  #               return 0
  #           if n > len(coins):
  #               return float('inf')
  #           if dp[n][target] != -1:
  #               return dp[n][target]
  #           t1 = float('inf')
  #           t2 = float('inf')
  #           if coins[n-1] <= target:
  #               dp[n][target] =  min(1 + solve(n, target+coins[n-1]),  solve(n+1, target))
  #           else:
  #               dp[n][target] = solve(n+1, target)
  #           return dp[n][target]
          
          
  #       solve(1, 1)
  #       print(dp)
  #       return dp[len(coins)][amount]