def longestCommonSeq(text1, text2):
  dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]
  def solve(i, j):
      if i >= len(text1) or j >= len(text2):
          return 0
      
      if dp[i][j] != -1:
          return dp[i][j]
          
      if text1[i] == text2[j]: 
          dp[i][j] =  1 + solve(i+1, j+1)
          return dp[i][j]
      else:
          t1 = solve(i+1, j)
          t2 = solve(i, j+1)
          dp[i][j] = max(t1, t2)
          return dp[i][j]
  return solve(0,0)
      
text1= "bcdeab"
text2 = "ace"

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

# time complexity here -  in recursion, its exponentail ...2^n and by memo it comes to o(n2)
# here main thought process is that if any letters is equal then simple aage k
# chars pe dekho then  here check for a matches with i+1 and all kar kar ke...then c k sath dekho
# if matches then ok else e k consider kro so a e ace diff combo hm dekh rhe h using recursion
# thats why frst i+1, j and then i, j+1

# in second version,,main thought is neche se upar chalo ap...and n+1, n2+1 ko lekr string me 
# n1-1, n2-1 se compae krke filling matrix
# If the two strings have no matching characters, so the last line always gets executed, the the time bounds are binomial coefficients, which (if m=n) are close to 2^n.