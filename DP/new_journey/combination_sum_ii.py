def combo2(nums, target):
  result = []
  def solve(index, target, res):
    if target == 0:
      result.append(res[:])
      return
    if index >= len(nums):
      return
      
    if nums[index] <= target:
      res.append(nums[index])
      solve(index+1, target-nums[index], res)
      res.pop()

    solve(index+1, target, res)
  solve(0, target, [])
  return result

candidates = [10,1,2,7,6,1,5]
target = 8
print(combo2(candidates, target))