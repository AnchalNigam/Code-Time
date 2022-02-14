ans = 0
count = 0
diff = 0
for i in range(len(nums)-1):
  currDiff = nums[i+1] - nums[i]
  if currDiff ==  diff:
      count += 1                
  else:
      diff = currDiff
      if count >= 2:
          dp[i] = dp[i] + (count-1)
          
      count = 1

if count >= 2:
  ans += count
