def longestCommonString(text1, text2):
  dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
  maxx = 0
  for i in range(1, len(text1)+1):
    for j in range(1, len(text2)+1):
      if text1[i-1] == text2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
        if(maxx<dp[i][j]):
          maxx=dp[i][j]
                
      else:
        dp[i][j] = 0
  return maxx

text1 = "abcde"
text2 = "ace"

print(longestCommonString(text1, text2))
