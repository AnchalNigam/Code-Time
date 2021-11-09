# def maxSum(k, arr):
#   def maxSumRecursion(n, k):
#     if n == 0:
#       return 0
#     if arr[n-1] <= k:
#       return max(arr[n-1] + maxSumRecursion(n, k-arr[n-1]), maxSumRecursion(n-1, k))
#     else:
#       return  maxSumRecursion(n-1, k)
#   return maxSumRecursion(len(arr), k)

# k = 10
# arr = [2,3,4]
# print(maxSum(k, arr))


def maxSum(k, arr):
  dp = [[0 for i in range(k+1)] for j in range(len(arr)+1)]
  for i in range(1, len(arr)+1):
    for j in range(1, k+1):
      if arr[i-1] <= j:
        dp[i][j] = max(arr[i-1] + dp[i][j-arr[i-1]], dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
  return dp[i][j]


k = 10
arr = [2,3,4]
print(maxSum(k, arr))
