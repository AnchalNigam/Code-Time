class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dp = [[-1 for idx in range(B+1)]for idx in range(len(A)+1)]
        def isSubset(A, B, n):
            if n == -1 and B == 0:
                return 1
            elif n == -1 and B != 0:
                return 0
            if dp[n][B] != -1:
                return dp[n][B]
            if A[n] <= B:
                dp[n][B] = isSubset(A, B-A[n], n-1) or isSubset(A, B, n-1)
                return dp[n][B]
            else:
                dp[n][B] = isSubset(A, B, n-1)
                return dp[n][B]
             
        return isSubset(A, B, len(A)-1)
 
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
        dp[i][j] = dp[i-1][j-A[i-1]] or dp[i-1][j]
      else:
         dp[i][j] = dp[i-1][j]
      
  print(dp)
  return dp[n][B]
A = [3, 34, 4, 12, 5, 2]
B = 1
print(solve(A, B))

def solve(A, B):
  dp = [[0 for idx in range(B+1)]for idx in range(len(A)+1)]
  count = [0]
  def isSubset(A, B, n):
      if n == -1 and B == 0 or B == 0:
          return 1
      elif n == -1 and B != 0:
          return 0
      if A[n] <= B:
        if(isSubset(A, B-A[n], n-1)):
          count[0] += 1
      if(isSubset(A, B, n-1)):
        count[0] += 1    
  isSubset(A, B, len(A)-1)
  return count
A = [2,3,5,6,8,10]
B = 20
print(solve(A, B))


# in top down approach, we basically maintain table for all the combos like [1,2,7] so hum sbka
# nikalnge like if there is 1 element in array so whether sum is 1, sum is 2 is fesible or not
# so ek table prepare with all the combos. n - 1 to 3, sum - 1 to 10
# same concept include that element in subset then exclude that element 
# - dp[i-1][j-A[i-1]] or dp[i-1][j]. [i] means n (no of elem) with previous i result
#  ad j is sum and prepare.recursion based top down is written like
# isSubset(A, B-A[n], n-1) = dp[i-1][j-A[i-1]] [previous wala k lie ab nikale and sun got reduce]