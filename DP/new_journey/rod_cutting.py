n = 8
dp = [[0 for idx in range(n+1)]for idx2 in range(n+1)]
l = [idx for idx in range(1, n+1)]
prices = [1, 5, 8, 9, 10, 17, 17, 20]
for i in range(1, n+1):
  for j in range(1, n+1):
    if l[i-1] <= j:
      dp[i][j] = max(prices[i-1] + dp[i][j-l[i-1]], dp[i-1][j])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][n])

# in this first think of smaller input , i think of 0 rod then 2 input length (2m rod)
# n=2 price=[1,5], then build recursion sol then make top down approach using recursion 
# see aditya video for more clarity

# revursion
def solve(price, n):
  l = [idx for idx in range(1, n+1)]
  def recursion(rodL, n):
    if rodL == 0 or n == 0:
      return 0
    if l[n-1] <= rodL:
      return max(price[n-1] + recursion(rodL- l[n-1], n), recursion(rodL, n-1))
    else:
      return recursion(rodL, n-1)
  return recursion(n, n)
prices = [3,5]
print(solve(prices, 2))
