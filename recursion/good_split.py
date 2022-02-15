

# def goodSplit(s):
#   count = 0
#   def helper(s1, s2):
#     dic = {}
#     dic2 = {}
#     count1 = 0
#     count2 = 0
#     for char in s1:
#       if char not in dic:
#         count1 += 1
#         dic[char] = 1
#       else:
#         dic[char] += 1
#     for char in s2:
#       if char not in dic2:
#         count2 += 1
#         dic2[char] = 1
#       else:
#         dic2[char] += 1
#     return count1 == count2

#   for i in range(len(s)):
#     if(helper(s[:i+1], s[i+1:])):
#       count += 1
#   return count

# s = "aacaba"
# print(goodSplit(s))
# o(n2) as per my knowledge complexity hga so time limit exceeded in leetcode

    



def goodSplit(s):
  uniqueCount1 = 0
  uniqueCount2 = 0
  dic1 = {}
  dic2 = {}
  count = 0
  for char in s:
    if char not in dic1:
      uniqueCount1 += 1
      dic1[char] = 1

    else:
      dic1[char] += 1
  print(uniqueCount1, dic1)
  for char in s:
    if char not in dic2:
      uniqueCount2 += 1
      dic2[char] = 1
    else:
      dic2[char] += 1
    dic1[char] -= 1
    if dic1[char] == 0:
      uniqueCount1 -= 1
    if uniqueCount1 == uniqueCount2:
      count += 1
  return count



s = "aabcd"
print(goodSplit(s))

# O(n) time complexity -  done by me  - yoooo