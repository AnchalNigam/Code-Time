# 1st way
# def isAnagram(self, s: str, t: str):
#   if ''.join(sorted(list(s))) == ''.join(sorted(list(t))):
#     return True
#   return False



# 2nd way - hash map
dic1 = {}
dic2 = {}
def isAnagram():
  if(len(s) != len(t)):
    return False
  s = "ac"
  t = "bb"

  for char in s:
    if char in dic1:
      dic1[char] += 1
    else:
      dic1[char] = 1

  for char in t:
    if char not in dic1:
      return False
    else:
      if char in dic2:
        dic2[char] += 1
      else:
        dic2[char] = 1
  for key in dic1:
    if dic1[key] != dic2[key]:
      return False
  return True

print(isAnagram())
  
