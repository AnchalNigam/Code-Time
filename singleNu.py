def getSingleNum():
  nums = [1]
  nums.sort()
  print(nums)
  flag = False
  if len(nums) == 1:
      return nums[0]
  for idx in range(len(nums)-1):
    if nums[idx] != nums[idx+1] and not flag:
      return nums[idx]
    elif nums[idx] != nums[idx+1]:
      flag = False
    else:
      flag = True
  if not flag:
    return nums[idx+1]

print(getSingleNum())