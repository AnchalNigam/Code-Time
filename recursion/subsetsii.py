def subsetsII(nums):
  n = len(nums)
  result = []
  visited = {}
  nums.sort()
  def solve(start, res):

    if(start >= n):
      print(res)
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
    # print(res, 'res')

    res.pop()
    solve(start+1, res)
  solve(0,[])
  return result

print(subsetsII([1,2,3]))

# at every backtracking, we popped out the last elem and then start will be left ip \..
# just think of your tree 