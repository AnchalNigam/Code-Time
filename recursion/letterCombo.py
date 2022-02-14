def letterCombo(digits):
  result = []
  dic = {
    "1" : [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m" ,"n", "o"],
    "7": ["p", "q", "r"],
    "8": ["s", "t", "u"],
    "9": ["v", "w", "x", "z"]
  }
  ip = []

  for i in digits:
    ip.append(dic[i])
  def solve(i, j, res):
    if(len(res) == len(ip)):
      result.append(res)
      return
    if i >= len(ip) or j >= len(ip[i]):
      return False
  
    res += ip[i][j]
    # print(res, 'res')
    solve(i+1, 0, res)
    res = res[:-1]
    solve(i, j+1, res)
    res = res[:-1]
  solve(0, 0, "")
  return result

print(letterCombo("239"))