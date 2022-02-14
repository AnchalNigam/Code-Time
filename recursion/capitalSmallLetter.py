from unittest import result


def capitalSmall(s):
  result = []
  n = len(s)
  def solve(i, res):
    if i >= n:
      result.append(res)
      return
    
    if s[i].isalpha():
      res += s[i]
      solve(i+1, res)
      res = res[:-1]
      if(s[i].isupper()):
        res += s[i].lower()
      elif s[i].islower():
        res += s[i].upper()

      solve(i+1, res)
      res = res[:-1]
    else:
      res += s[i]
      solve(i+1, res)
      res = s[:-1]
  solve(0, '')
  return result
   
s = "a1b2"

print(capitalSmall(s))