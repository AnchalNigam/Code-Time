# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         dp = [[-1 for idx in range(B+1)]for idx in range(len(A)+1)]
#         def isSubset(A, B, n):
#             if n == -1 and B == 0:
#                 return 1
#             elif n == -1 and B != 0:
#                 return 0
#             if dp[n][B] != -1:
#                 return dp[n][B]
#             if A[n] <= B:
#                 dp[n][B] = isSubset(A, B-A[n], n-1) or isSubset(A, B, n-1)
#                 return dp[n][B]
#             else:
#                 dp[n][B] = isSubset(A, B, n-1)
#                 return dp[n][B]
             
#         return isSubset(A, B, len(A)-1)
 
# above one is recursion and memo and below one is top down approach
def solve(A, B):
  dp = [[-1 for idx in range(B+1)]for idx in range(len(A)+1)]
  n = len(A)
  for i in range(n+1):
    for j in range(B+1):
      if i == 0:
        dp[i][j] = False
      if j == 0:
        dp[i][j] = True

  for i in range(1, n+1):
    for j in range(1, B+1):
      if A[i-1] <= j:
        dp[i][j] = dp[i][j-A[i-1]] or dp[i-1][j]
      else:
         dp[i][j] = dp[i-1][j]
      
  print(dp)
  return dp[n][B]
A = [3, 34, 4, 12, 5, 2]
B = 1
print(solve(A, B))