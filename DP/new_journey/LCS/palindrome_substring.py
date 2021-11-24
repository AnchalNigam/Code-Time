# def longestCommonSequence(text1, text2):
#   dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
#   maxx = 0
#   maxIndexi = 0
#   maxIndexj = 0
#   for i in range(1, len(text1)+1):
#     for j in range(1, len(text2)+1):
#       if text1[i-1] == text2[j-1]:
#         dp[i][j] = 1 + dp[i-1][j-1]
#         if(maxx<dp[i][j]):
#           maxx=dp[i][j]
#           maxIndexi = i
#           maxIndexj = j
#       else:
#         dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#   print(maxIndexi, maxIndexj, maxx)
#   print(dp)
#   return text1[len(text1)-maxIndexj: maxIndexi]

# s = "aacabdkacaa"
# b = s[::-1]
# print(longestCommonSequence(s, b))

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

s = "aacabdkacaa"

print(palindromicSequence(s))


#here basically lcs usage is taken, first we are maing b string reverse of a and then same
#lcs logic lagaya 

# NOTHING WORKED