def longestOnes(nums, k):
  l = 0
  r = 0
  maxVal = 0
  while r < len(nums):
    if nums[r] == 0:
      k -= 1
    if k >= 0:
      maxVal = max(maxVal, r-l+1)
    while k < 0:
      if nums[l] == 0:
        k += 1
      l += 1
    r += 1
  return maxVal
      