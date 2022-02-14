def subsetsII(nums):
  n = len(nums)
  result = []
  visited = {}
  nums.sort()
  def solve(start, res):

    if(start >= n):
      resStr = ''.join(map(str, res))
      try:
        if not visited[resStr]:
          visited[resStr] = True
      except KeyError:
        result.append(res[:])
        visited[resStr] = True
      return result
    res.append(nums[start])
    solve(start+1, res)
    res.pop()
    solve(start+1, res)
  solve(0,[])
  return result

print(subsetsII([4,4,4,1,4]))

# at every backtracking, we popped out the last elem and then start will be left ip \..
# just think of your tree 