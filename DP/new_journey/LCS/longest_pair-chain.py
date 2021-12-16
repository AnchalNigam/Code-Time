def longestPairChange(pairs):
  dp = [0 for idx in range(len(pairs))]
  pairs.sort()
  oMaxx = 0
  for i in range(len(pairs)):
    maxx = 0
    for j in range(i):
      if pairs[j][1] <= pairs[i][0]:
        if maxx < dp[j]:
          maxx = dp[j]

    dp[i] = maxx + 1
    if oMaxx < dp[i]:
      oMaxx = dp[i]  
  return oMaxx



pairs = [[1,2],[7,8],[4,5]]
print(longestPairChange(pairs))

# this is variation of LCS, here basically we are just sorting as its saying in any order can 
# it come. the only thing is b < c . so apply LCS