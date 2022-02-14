def permutations2(nums):
  result = []

  def solve(res, ip, visited):
    if len(ip) == 0:
      resStr = ''.join(map(str, res))
      try:
        if not visited[resStr]:
          visited[resStr] = True
      except KeyError:
        result.append(res[:])
        visited[resStr] = True
      return

    for i in range(len(ip)):
      if(i>0 and ip[i] == ip[i-1] and not visited[ip[i-1]]):
          continue
      visited[ip[i]] = True
      res.append(ip[i])
      solve(res, ip[:i]+ip[i+1:], visited)
      res.pop()
      visited[ip[i]] = False
    return
  solve([], nums, {})
  return result

print(permutations2([1,2,1]))