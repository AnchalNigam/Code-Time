dp = [-1 for idx in range(4)]
def pairParty(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  if dp[n-1] == -1:
    dp[n-1] = pairParty(n-1)
  if dp[n-2] == -1:
    dp[n-2] = pairParty(n-2)
  return dp[n-1] + (dp[n-2] * (n-1))
print(pairParty(4))