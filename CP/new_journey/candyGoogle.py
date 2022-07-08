T = int(input())
def parenthesis(L, M):
  x = min(L,M)
  if x == 0:
    return 0
  dp = [0 for i in range(x+1)]
  dp[1] = 1
  for i in range(2, x+1):
    dp[i] = dp[i-1]+1 + ((i-1))
  return dp[x]



for t in range(T):
  L, R = list(map(int,input().split()))
  print(f"Case #{t+1}: {parenthesis(L, R)}")