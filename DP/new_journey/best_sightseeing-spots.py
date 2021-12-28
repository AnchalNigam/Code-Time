def maxScoreSightseeingPair(self, values: List[int]) -> int:
  i1 = 0
  i2 = 1
  maxVal = values[i1] + values[i2] + i1 - i2
  for idx in range(2, len(values)):
      sum1 = values[i1] + values[idx] + i1 - idx
      sum2 = values[i2] + values[idx] + i2 - idx
      if sum1 >= sum2:
          i2 = idx
          maxVal = max(maxVal, sum1)
      else: 
          i1 = i2
          i2 = idx
          maxVal = max(maxVal, sum2)    
  return maxVal

# here approach is taken by seeing at smaller input, if smaller input then how we are approaching
# when new elem comes then pevious i1 and i2 we have taken , we compare the same with new i2,
# whihever is big, we take that i1 and i2 like i1=0, i2=0, now 5 comes, we take 5 as i2
# add vaues[i1]+val[i2]+i2-i2 and then which gives greater res, we store that i1 and i2 and 
# also maxVal for future compare. main thing which leanrned is think of smaller ip