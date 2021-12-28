# def jumpGame(nums):
#   n = len(nums)
#   dp = [0 for idx in range(n)]
#   i = 1
#   j = 0
#   while i < n:
#       minVal = float('inf')
#       j = 0
#       while j < i:
#         if nums[j] >= i-j:
#           minVal = min(dp[j]+1, minVal)
#         j += 1
#       dp[i] = minVal
#       i += 1
#   if dp[n-1] == float('inf'):
#     return -1
#   return dp[n-1]




def jumpGame(nums):
    A, n = nums, len(nums)
    jumps, end, farthest = 0, 0, 0, # The current end and current farthest 
    for i in range(n-1):
        farthest = max(farthest, i+A[i])
        # if farthest >= n-1:
        #     return jumps
        if i == end:
            print(farthest, i, end)
            jumps += 1
            end = farthest
    return jumps

nums = [2,4,1,1,4]
print(jumpGame(nums))

# here main logic is we have ladders, we are storng max ladder as it will help us
# if previous ladder finishes so we jump to max stored ladder

