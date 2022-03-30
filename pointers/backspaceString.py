def backspaceString(s, t):
  # s = "ab#c"
  # t = "ad#c"
  res1 = []
  for char in range(len(s)):
    if s[char] != "#" :
      res1.append(s[char])
    elif len(res1) > 0:
      res1.pop()

  res2 = []
  for char in range(len(t)):
    if t[char] != "#" :
      res2.append(t[char])
    elif len(res2) > 0:
      res2.pop()
  return res1 == res2
  
        
def backspaceString(s, t):
  p1 = len(s)-1
  p2 = len(t)-1
  skip_s = 0
  skip_t = 0
  while p1 >= 0 or p2 >= 0:
    while p1 >= 0:
      if s[p1] == "#":
        skip_s += 1
        p1 -= 1
      elif skip_s > 0:
        p1 -= 1
        skip_s -= 1
      else: 
        break
    # print(p2)
    while p2 >= 0:
      if t[p2] == "#":
        skip_t += 1
        p2 -= 1
        # print('00101', p2)
      elif skip_t > 0:
        p2 -= 1
        skip_t -= 1
        # print(p2, '11')
      else: 
        # print(p2, '000')
        break
    # print(p2, 'hii', p1)   
    if(p1 >= 0) != (p2 >= 0):
      return False  
    if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
      return False
  
    p1 -= 1
    p2 -= 1
  return True

# frst version is your stack ersion ..we will put data if we get backlash remove it and end me compare kr lo
# simple one but using space
# second one is start with last string and check if its same or not
# if yes, then continue else false. if we see any # then we add skip += 1 and then again 
# if skip > 0 toh usko skip kro in this way pointers move kr rhe hai
# and last me man lo ek empty h gya ek non empty h gya toh bhi false hga 
# and see if p1 >= 0 and p2 >= 0 and s[p1] != t[p2], ye wale condition me p1>=0 and all islie
# lagaya because aisa h skta h ki while loop me p1 -1 pahuch gya toh because shuru me kafi # h0
# thats why ye condition hai...
# time complexity - o(n), space - o(1)

