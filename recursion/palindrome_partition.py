

def palindromePartition(s):
  result = []
  n = len(s)
  def solve(s, res):
    if len(s) == 0:
      result.append(res[:])
      return
    for i in range(0, len(s)):
      tillS = s[:i+1]
      if tillS == tillS[::-1]:
        res.append(tillS)
        solve(s[i+1:], res)
        res.pop()

    

  solve(s, [])
  return result

s="aba"
print(palindromePartition(s))

