# def isSubsequence(s, t):
#   dp = [[False for i in range(len(t)+1)] for j in range(len(s)+1)]
#   for i in range(1, len(s)+1):
#       for j in range(1, len(t)+1):
#           if s[i-1] == t[j-1]:
#               dp[i][j] = 1 + dp[i-1][j-1]
#           else:
#               dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#   return dp[len(s)][len(t)] == len(s)


def isSubsequence(s, t):
  if len(s) == 0:
    return True
  matchingCount = len(s)
  counter = 0
  for i in range(len(t)):
    if s[counter] == t[i]:
        matchingCount -= 1
        counter += 1
    if matchingCount == 0:
        break
  return matchingCount == 0

s = "AXY"
t = "ADXCPY"

print(isSubsequence(s, t))