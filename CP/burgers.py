# T = int(input())
# result = []
# def burgersCount(patty, buns):
#   return min(patty, buns)
    
# for t in range(T):
#   patty, buns =  list(map(int,input().split()))
#   result.append(burgersCount(patty, buns))

# for res in result:
#   print(res)

# T = int(input())
# result = []
# def chefWait(K, X):
#   return (K*7)-X
    
# for t in range(T):
#   K, X =  list(map(int,input().split()))
#   result.append(chefWait(K, X))

# for res in result:
#   print(res)

# T = int(input())
# result = []
# def encoding(n, S):
#   encoder = {
#     "00": 'A',
#     "01": 'T',
#     "10": 'C',
#     "11": 'G'
#   }
#   encodedStr = ""
#   for i in range(0, n-1, 2):
#     encodedStr += encoder[S[i: i+2]]
#   return encodedStr
    
    
# for t in range(T):
#   n =  int(input())
#   S = input()
#   result.append(encoding(n, S))

# for res in result:
#   print(res)

# T = int(input())
# result = []
# import math
# def joiningDate(N, K):
#   totalJoiningDates = math.ceil(N/5)
#   x = K // 5
#   droppedCandidateJoiningSlot = x if K%5 == 0 else x+1
#   return totalJoiningDates - droppedCandidateJoiningSlot
    
# for t in range(T):
#   N, K = list(map(int,input().split()))
#   result.append(joiningDate(N, K))

# for res in result:
#   print(res)


T = int(input())
result = []
def distinctPalindrome(N, X):
  chars = "abcdefghijklmnopqrstuvwxyz"
  # print(len(chars))
  distinctCharPossible = 0
  y = N//2
  if N % 2 == 0:
    distinctCharPossible = y 
  else:
    distinctCharPossible = y + 1

  if X > distinctCharPossible:
    return -1
  c = 0
  strr = ""
  while c < y:
    strr += chars[(c%26)+25]
    c += 1
  # print(strr, 'strr')
  reverseStrr = strr[::-1]
  if N%2 != 0:
    strr += chars[25]
  strr += reverseStrr
  return strr


for t in range(T):
  N, X = list(map(int,input().split()))
  result.append(distinctPalindrome(N, X))

for res in result:
  print(res)