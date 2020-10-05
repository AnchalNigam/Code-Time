def fibonacciModified(t1, t2, n):
  dp = [-1 for idx in range(n)]
  dp[0] = t1
  dp[1] = t2
  def getFib(n):
    if n == 0:
        return t1
    if n == 1:
        return t2
    if dp[n-1] == -1:
      dp[n-1] = getFib(n-1)
    if dp[n-2] == -1:
      dp[n-2] = getFib(n-2)
  
    return (dp[n-1])**2 + dp[n-2]
  return getFib(n)
print(fibonacciModified(1,2,3))
