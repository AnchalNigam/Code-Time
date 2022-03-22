def lengthOfLongestSubstring(s):
  if len(s) == 0:
      return 0
  l = 0
  r = 1
  dic = {}
  dic[s[l]] = 1
  c = 1
  omax = float('-inf')
  while l <= r and r < len(s):
      # print(dic, c)
    if s[r] not in dic:
      c += 1
      dic[s[r]] = 1
      r += 1
    else:
      omax = max(omax, c)
      c -= 1
      del dic[s[l]] 
      l += 1 
          
  omax = max(omax, c)
  return omax


# here sliding window techniue is used..basically we are expanding our window till we find duplicate
# duplicacy count we are maintaing using dic..now if we find any duplicate 
# it means this widow is not correct window, we should change our window..now if the first 
# element is responsible for this duplicacy like in case "dvdf", at 2 idx d is suplicate
# meaning frst elemnt is responsible so just remove that element from the window by expanding
# l+=1 and remove it also from dic and count reduce by 1...so new valid comes in play
# idx 1 to 2...now ake another eg "pwwkew" here at idx 2 frst elemnt is not responsible
# bt still as is asking for substring we have to discard and will try to find which
# element is actually responsible for this duplicacy by l+= 1, dic se remove krke and count reduce
# krke ..we dont expand r till we find culprit so in this way, window is maintained