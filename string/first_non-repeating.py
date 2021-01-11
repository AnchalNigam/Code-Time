def firstUniqChar(s: str) -> int:
  dic = {}
  for idx in range(len(s)):
    if s[idx] not in dic:
      dic[s[idx]] = [1,idx]
    else:
      dic[s[idx]][0] += 1 
  for key in dic:
    if dic[key][0] == 1:
      return dic[key][1]
  return -1

print(firstUniqChar("leetcode"))
      