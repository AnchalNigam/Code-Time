# recursive
# def longIncreasingSeq(arr):
#   def solve(n, last):
#     if n == 0:
#       return 0
#     if arr[n-1] < last:
#       return max(1+solve(n-1, arr[n-1]), solve(n-1, last))
#     else:
#       return solve(n-1, last)
#   return solve(len(arr), float('inf'))

# memoization
# didn't get success
# def longIncreasingSeq(arr):
#   # dp = [[0 for i in range(len(arr)+1)] for j in range(len(arr)+1)]
#   # for i in range(1, len(arr)+1):
#   #   for j in range(1, len(arr)+1):
#   #     if arr[i-1] < arr[j-1]:
#   #       dp[i][j] = max(1+dp[i-1][j-1], dp[i-1][j])
#   #     else:
#   #       dp[i][j] =  dp[i-1][j]
#   # print(dp)
#   # return dp[len(arr)][len(arr)]
#   dp = [0 for i in range(len(arr))]
#   dp[0] = 1
#   def solve(n, last):
#     if n == 0:
#       return 0
#     if dp[n-1] != 0:
#       return dp[n-1]
#     if arr[n-1] < last:
#       dp[n-1] = max(1+solve(n-1, arr[n-1]), solve(n-1, last))
#       return dp[n-1]
#     else:
#       dp[n-1] = solve(n-1, last)
#       return dp[n-1]
#   solve(len(arr), float('inf'))
#   print(dp)
#   return dp[len(arr)-1]


def longIncreasingSeq(arr):
  dp = [0] * len(arr)
  oMaxx = 0
  for i in range(0, len(arr)):
      # do for each element in sublist `arr[0…i-1]`
      maxx = 0
      for j in range(i):
          # find the longest increasing subsequence that ends with `arr[j]`
          # where `arr[j]` is less than the current element `arr[i]`
          if arr[j] < arr[i]:
            if dp[j] > maxx:
              maxx = dp[j]
      dp[i] = maxx + 1
      if oMaxx < dp[i]:
        oMaxx = dp[i]
  return oMaxx
# didn't get success
# def longIncreasingSeq(arr):
#   dp = [0 for i in range(len(arr))]
#   dp[0] = 1
#   def solve(n, last):
#     if n == len(arr):
#       return 0
#     if dp[n-1] != 0:
#       return dp[n-1]
#     if arr[n-1] > last:
#       dp[n] = max(1+solve(n-1, arr[n-1]), solve(n-1, last))
#       return dp[n]
#     else:
#       dp[n] = solve(n-1, last)
#       return dp[n]
#   solve(0, 0)
#   print(dp)
#   return dp[len(arr)-1]

# nums = [1,3,6,7,9,4,10,5,6]

# nums = [13,1,3,4,8,19,17,8,0,20,14]
nums = [10, 22, 9, 33]
print(longIncreasingSeq(nums))


# https://www.youtube.com/watch?v=odrfUCS9sQk 
# in this we are seeing current point elem with previous one and whoever is max saving that
# and then updated current with +1
# here the idea is - look at 33 as 33 is geater than with every number before it but, kis 
# previous pair me it should add, 9 or 10,22 or 10 which one is maxx till its element
# we will consider. like 10, 22 tak max seq 2 tha whereas 9 pe ax seq only 1 so profitable
# pair is 10,22 as its have max seq. so concept is like this