
T = int(input())
result = []
def longestPalindrome(s):
  n = len(s)
  ans = ""
  maxLength = 0
  dp = [[0]*n for i in range(n)]
  for i in range(n-1, -1, -1):
    for j in range(i, n):
      if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1] == 1):
        dp[i][j] = 1
        if ans == "" or maxLength < j-i+1:
          maxLength = j-i+1
          ans = s[i: j+1]
  return ans

for t in range(T):
  N = map(int, input().split())
  s = input()
  result.append(longestPalindrome(s))

for res in result:
  print(res)

