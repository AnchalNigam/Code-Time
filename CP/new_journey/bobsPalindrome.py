T = int(input())
def isPalindrome(s):
  dic = {}
  for char in s:
    if char not in dic:
      dic[char] = 1
    else:
      dic[char] += 1
  even = 0
  odd  = 0
  for key, value in dic.items():
    if value % 2 == 0:
      even += 1
    else:
      odd += 1
  if len(s)%2 == 0 and odd > 0:
    return False
  elif len(s)%2 != 0 and odd > 1:
    return False
  return True
def countPalindrome(S, Q, indexes):
  count = 0
  for x, y in indexes:
    if (isPalindrome(S[x-1: y])):
      count += 1
  return count


for t in range(T):
  N, Q = list(map(int,input().split()))
  S = input()
  indexes = []
  for ques in range(Q):
    indexes.append(list(map(int,input().split())))

  print(f"Case #{t+1}: {countPalindrome(S, Q, indexes)}")