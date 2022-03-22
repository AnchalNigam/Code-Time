def LongKUniqueSubstring(s, k):
  l = 0
  r = 0
  dic = {}
  M = 0
  res = float('-inf')
  while r < len(s):
      if s[r] not in dic:
          dic[s[r]] = 1
          M += 1
      else:
          dic[s[r]] += 1
      if M == k:
          res = max(res, r-l+1)
      while M > k:
          if dic[s[l]] == 1:
              del dic[s[l]]
              M -= 1
          else:
              dic[s[l]] -= 1
          l += 1
      r += 1
  return -1 if res == float('-inf') else res

# Time complexity o(n) 
# space - o(n)
# majorly variable size window ka template..here if m > k i.r ur condition then we loop till that 
# condition m >k kam na h jaye when less then againn r+=1 shuru..so keep this logic in mind