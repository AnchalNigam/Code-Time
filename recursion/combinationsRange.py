def combinationRange(n, k):
  nums = [i for i in range(1, n+1)]
  print(nums)
  result = []
  def solve(start, res):
    if len(res) == k:
      result.append(res[:])
      return
    if start >= n:
      return
    res.append(nums[start])
    # print(start, res, 'check')
    solve(start+1, res)
    res.pop()
    solve(start+1, res)
    print(res, 'res')
  solve(0, [])
  return result

print(combinationRange(4,2))


  