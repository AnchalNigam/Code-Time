def combo(nums, target):
  count = [0]
  result = []
  def solve(i,target, res):
    if target == 0:
      result.append(res[:])
      return
    if(i >= len(nums)):
      return 
    if nums[i] <= target:
      res.append(nums[i])
      solve(i, target-nums[i],res)
      res.pop()
    solve(i+1, target, res)
    
    

  solve(0, target, [])
  return result


nums = [2,3,5]
print(combo(nums, 8))