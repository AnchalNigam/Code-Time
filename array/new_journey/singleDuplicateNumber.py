from typing import List
def duplicate(nums):
  nums.sort()
  for i in range(len(nums)-1):
      if nums[i] == nums[i+1]:
          return nums[i]
  
# basic sorting hai
def findDuplicate(nums):
  i = 0
  n = len(nums)
  while i < n:
      # print(nums)
      if(nums[i] != i+1):
          if(nums[nums[i]-1] == nums[i]):   
              i += 1
          else:
              temp = nums[nums[i]-1]
              nums[nums[i]-1] = nums[i]
              nums[i] = temp
      else:
          i += 1
  return nums[n-1]

# above solutn is applying cyclic sort knowledge -  basically as they said 1 to n h rhega
# toh har number k apne jagah pe pahuchao na..1 k 0th pe, 2 ko 1th index pe, 3 ko 2nd and so on
# so ab j apne jagah pe aajyange and last me wo rhnge j duplicates hai toh last wala send kr de
# ko consider kro
def findDuplicate(nums: List[int]) -> int:
  for i in range(len(nums)):
    temp = abs(nums[i])-1
    if nums[temp] > 0: 
      nums[temp] *= -1
    else:
      return abs(nums[i])
  return -1

# above soltn wo negative kr do j negative h mns wo repeated hai toh return mar do turnt