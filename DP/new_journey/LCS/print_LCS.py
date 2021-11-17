# not got success, just a try

# def longestCommonSequence(text1, text2):
#   dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
#   res = [""]
#   def solve(n, m):
#     if n == 0 or m == 0:
#       return 0
#     if dp[n][m] != 0:
#       return dp[n][m]
#     if text1[n-1] == text2[m-1]:
#       res[0] = text1[n-1] + res[0]
#       dp[n][m] = 1 + solve(n-1, m-1)
#       return dp[n][m]
#     else:
#       dp[n][m] = max(solve(n, m-1), solve(n-1, m))
#       return dp[n][m]
#       # if(dp[n][m-1] == 0):
#       #   dp[n][m-1] = solve(n, m-1)
#       # if(dp[n-1][m] == 0):
#       #   dp[n-1][m] = solve(n-1, m)
#       # if(dp[n-1][m] > dp[n][m-1]):
#       #   return dp[n-1][m]
#       # else:
#       #   return dp[n][m-1]
#   solve(len(text1), len(text2))
#   return res[0]

# text1 = "abbcdgf"
# text2 = "bbadcgf"

# print(longestCommonSequence(text1, text2))
def printLCS(text1, text2):
  dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
  for i in range(1, len(text1)+1):
    for j in range(1, len(text2)+1):
      if text1[i-1] == text2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
  i = len(text1)
  j = len(text2)
  res = []
  while(i > 0 and j > 0):
    if(text1[i-1] == text2[j-1]):
      res.append(text1[i-1])
      i -= 1
      j -= 1
    else:
      if dp[i-1][j] > dp[i][j-1]:
        i -= 1
      else:
        j -= 1
  return res[::-1]

text1 = [1, 2, 3, 4, 1]
text2 = [3, 4, 1, 2, 1, 3]

print(printLCS(text1, text2))

      
