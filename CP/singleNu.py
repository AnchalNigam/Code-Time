def getSingleNum():
  nums = [4,1,2,1,2]
  nums.sort()
  flag = False
  for idx in range(len(nums)-1):
    if nums[idx] != nums[idx+1] and not flag:
      break
    elif nums[idx] != nums[idx+1]:
      flag = False
    else:
      flag = True
  if not flag:
    return nums[idx]
  return nums[idx]

print(getSingleNum())