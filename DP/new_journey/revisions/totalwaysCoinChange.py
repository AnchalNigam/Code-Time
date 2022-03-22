amount = 3
coins = [1,2,3]
dp = [[-1 for idx in range(amount+1)] for idx2 in range(len(coins)+1)]
for i in range(len(coins)+1):
  for j in range(amount+1):
    if i == 0 or j == 0:
      dp[i][j] = 0
    if i != 0 and j == 0:
      dp[i][j] = 1
def solve(n, amount):
  if amount == 0:
    return 1
  if amount < 0 or n > len(coins):
      return 0
  # print(n)
  if dp[n][amount] != -1:
      return dp[n][amount]
  
  if coins[n-1] <= amount:
      dp[n][amount] = solve(n, amount-coins[n-1]) +  solve(n+1, amount)
  else:
      dp[n][amount] = solve(n+1, amount)
  return dp[n][amount]

solve(1, amount)
print(dp)