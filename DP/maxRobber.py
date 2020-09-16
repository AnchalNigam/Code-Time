nums = [2,7,9,3,1]
# nums = [1,2,3,1]
# nums = [2,1]
# nums = [0,3,2,0]
# nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
N = len(nums)-1
M = [-1 for idx in range(N+1)]
M[N] = nums[N]
def maxRob(n):
  print(n, M)
  if n == N:
    return nums[N]
  if n >= N:
    return 0
  if M[n] == -1:
    M[n] = max(nums[n]+maxRob(n+2), 0+maxRob(n+1))
    print(n, M, 'andar')
  if n+2 > N:
    return max(nums[n]+0, 0+M[n+1])
  else:
    return max(nums[n]+M[n+2], 0+M[n+1])
print(M)
print(maxRob(0))
