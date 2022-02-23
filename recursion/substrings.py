s = "cbbd"
def palidromeLongestSubString(s):
  res = ""
  oRes = ""
  if(len(s) == 1):
      return s
  for i in range(len(s)):
      res = s[i]
      for j in range(i+1, len(s)):
          res += s[j] 
          if(res == res[::-1] and len(res) >= len(oRes)):
              oRes = res
  if len(oRes) == 0:
      return s[0]
  return oRes