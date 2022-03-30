def dutchNationalFlagAlgo(nums):
  low = 0
  mid = 0
  high = len(nums)-1
  while mid <= high:
    if nums[mid] == 0:
      nums[low], nums[mid] = nums[mid], nums[low]
      low += 1
      mid += 1
    elif nums[mid] == 1:
      mid += 1
    else:
      nums[mid], nums[high] = nums[high], nums[mid]
      high -= 1
  print(nums)
nums = [2,0,1]
dutchNationalFlagAlgo(nums)

# here main thought is we are maintaining three pointers. frst poiner is for 1 and others resp.
# if we encounter 0 then obvio low and mid me swap banta hai and increment both..mns low k pehle sare
# 0 hnge low and mid k beech 1 and high k bad 2 so with this thought swap increment is done
# code is quite simple. check! strivers video help
