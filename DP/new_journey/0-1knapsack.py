# recursive approach
# def solve(A, B, C):
#   def recursiveSol(n, C):
#     if n == 0 or C == 0:
#       return 0
#     if B[n-1] <= C:
#       return max(A[n-1] + recursiveSol(n-1, C-B[n-1]), recursiveSol(n-1, C) )
#     else:
#       return recursiveSol(n-1, C)
    
#   return recursiveSol(len(A), C)
# bottom-up - topdown (aditya) approach
def solve(A, B, C):
  dp = [[0 for i in range(C+1)] for j in range(len(A)+1)]
  for i in range(1, len(A)+1):
    for j in range(1, C+1):
      if B[i-1] <= j:
        dp[i][j] = max(A[i-1] + dp[i-1][j-B[i-1]], dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
  print(dp)
  return dp[len(A)][C]

A = [6, 10, 8]
B = [2, 5, 7]
C = 10

# A = [ 359, 963, 465, 706, 146, 282, 828, 962, 492 ]
# B = [ 96, 43, 28, 37, 92, 5, 3, 54, 93 ]
# C = 383
print(solve(A, B, C))


