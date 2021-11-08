c = [1, 2, 3]
n = 4
# recursion
# def solve(n, summation):
#       if n != 0 and summation == 0:
#         return 1
#       if n == 0 or summation == 0:
#           return 0
      
#       if c[n-1] <= summation:
#           return solve(n, summation - c[n-1]) + solve(n-1, summation)
#       else:
#           return solve(n-1, summation)
  
# print(solve(len(c), n))

# top down approach i wrote using recursion
dp = [[0 for idx in range(n+1)] for idx2 in range(len(c)+1)]
for i in range(len(c)+1):
  for j in range(n+1):
    if i == 0 or j == 0:
      dp[i][j] = 0
    if i != 0 and j == 0:
      dp[i][j] = 1

for i in range(1, len(c)+1):
  for j in range(1, n+1):
    if c[i-1] <= j:
      dp[i][j] = dp[i][j-c[i-1]] + dp[i-1][j]
    else:
      dp[i][j] = dp[i-1][j]
print(dp[len(c)][n])

#IN this, unbounded knapsack is there as one coin can be choose any number of times.so added
#all ways in recursion. same did in top down. for n!=0 and summartion 0,1 is taken after 
#visualiztn i put this condition. same fanda, think of np ip, smaller ip
# recursion and then top down