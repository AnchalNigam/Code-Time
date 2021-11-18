def palindromicSequence(s):
  b = s[::-1]
  dp = [[0 for i in range(len(b)+1)] for j in range(len(s)+1)]
  for i in range(1, len(s)+1):
    for j in range(1, len(b)+1):
      if s[i-1] == b[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  return dp[len(s)][len(b)]

s = "cbbd"

print(palindromicSequence(s))


#here basically lcs usage is taken, first we are maing b string reverse of a and then same
#lcs logic lagaya 