def jumpGame(nums):
  if(len(nums) == 1):
          return True
  j = len(nums) - 2
  n = len(nums) - 1
  flag = False
  while j >= 0:
      r = n-j
      if nums[j] >= r:
          n = j
          flag = True
      else:
          flag = False
      j -= 1
  return flag

# here weare starting from back if we ae able to reach that index then its feasible to react last as well
# r is required jumps