def countVowels(n):
  char = ['a', 'e', 'i', 'o', 'u']
  res = []
  def solve(out, index):
      if(index >= 5):
          return 
      if len(out) == n:               
          res.append(out)
          return
      if len(out) < n:
          solve(out+char[index], index)
          out[:-1]
      solve(out, index+1)
  solve("", 0)
  return len(res)

  # here nacktracking approach, like we are taking 1 elems again and again till constraint like 
  # in combinatn sum, target is constraint and here len(out) is constraint