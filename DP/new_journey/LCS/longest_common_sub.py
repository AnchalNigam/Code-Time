#recursion
# def longestCommonSequence(text1, text2):
#   def solve(n, m):
#     if n == 0 or m == 0:
#       return 0
#     if text1[n-1] == text2[m-1]:
#       return 1 + solve(n-1, m-1)
#     else:
#       return max(solve(n, m-1), solve(n-1, m))
#   return solve(len(text1), len(text2))

# recursion + memoization
# def longestCommonSequence(text1, text2):
#   dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
#   def solve(n, m):
#     if n == 0 or m == 0:
#       return 0
#     if dp[n][m] != 0:
#       return dp[n][m]
#     if text1[n-1] == text2[m-1]:
#       dp[n][m] = 1 + solve(n-1, m-1)
#       return dp[n][m]
#     else:
#       dp[n][m] = max(solve(n, m-1), solve(n-1, m))
#       return dp[n][m]
#   return solve(len(text1), len(text2))


#here time complezity in recursion is exponential and in memo it reduced to o(n*m). how? dont know

def longestCommonSequence(text1, text2):
  dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
  for i in range(1, len(text1)+1):
    for j in range(1, len(text2)+1):
      if text1[i-1] == text2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
  return dp[len(text1)][len(text2)]




text1 = "abcde"
text2 = "ace"

print(longestCommonSequence(text1, text2))
