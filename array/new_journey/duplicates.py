# approach 1
def duplicates(nums):
  dic = {}
  for idx in range(len(nums)):
    if nums[idx] in dic:
      return True
    else:
      dic[nums[idx]] = 1
  return False
  
# complexity - o(n) , space - o(n)

# approach 2
def duplicates(nums):
  nums.sort()
  for idx in range(len(nums)-1):
    if nums[idx] == nums[idx+1]:
      return True
  return False
  
# complexity - o(nlogn) , space - o(n)
