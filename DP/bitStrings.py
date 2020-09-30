
# how many ways does bitstring can be formed (0 or 1) so that no 1's should be consecutive
dp = [-1 for idx in range(4)]
def bitString(n):
  if n == 2:
    return 3
  if n == 1:
    return 2
  if dp[n-1] == -1:
    dp[n-1] = bitString(n-1)
  if dp[n-2] == -1:
    dp[n-2] = bitString(n-2)
  return dp[n-1] + dp[n-2]
print(dp) 
print(bitString(4))