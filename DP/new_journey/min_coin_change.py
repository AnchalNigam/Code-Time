coins = [411,412,413,414,415,416,417,418,419,420,421,422]
summation = 9864

# def minCoins(coins, summation):
#   def solve(n, summation):
#     if summation == 0:
#       return 0
#     if n == 0:
#       return float('inf')
#     if n == 1:
#       if (summation % coins[n-1]) == 0:
#         return summation // coins[n-1]
#       else:
#         return float('inf')
#     if coins[n-1] <= summation:
#       print('checked', n)
#       return min(1 + solve(n, summation-coins[n-1]), solve(n-1, summation))
#     else:
#       print('checked')
#       return solve(n-1, summation)
#   return solve(len(coins), summation)
# print(minCoins(coins, summation))

# recursion is failing on aboe ip. although it also passed for some ip but failed for this


def minCoins(coins, summation):
  dp = [[0 for idx in range(summation+1)] for idx2 in range(len(coins)+1)]
  for i in range(len(coins)+1):
    for j in range(summation+1):
      if i == 0:
        dp[i][j] = float('inf')
      if j == 0:
        dp[i][j] = 0

  for i in range(1, summation+1):
    if (i % coins[0]) == 0:
      dp[1][i] = i // coins[0]
    else:
      dp[1][i] = float('inf')

  for i in range(2, len(coins)+1):
    for j in range(1, summation+1):
      if coins[i-1] <= j:
        dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
  if(dp[len(coins)][summation] == float('inf')):
    return -1
  else:
    return dp[len(coins)][summation]

print(minCoins(coins, summation))
#this is working. this took diff approach to solve unbounded knapsack. here for 1 input as well
# we solved. check video for better clarity