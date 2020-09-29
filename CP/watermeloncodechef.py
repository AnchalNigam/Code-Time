T = int(input())
waterMelonArr = []
def waterMelon(intArr):
  summation = sum(intArr)
  if summation == 0:
    return 'YES'
  idx  = len(intArr)
  newSummation = 0
  while idx > 0:
    newElem = intArr[idx-1]-idx
    newSummation = sum(intArr) - intArr[idx-1] + newElem
    if newSummation == 0:
      return 'YES'
    elif newSummation < 0:
      newSummation = 0
    else:
      intArr[idx-1] = newElem
    idx -= 1
  return 'NO'
for t in range(T):
  N = input()
  intArr = list(map(int,input().split()))
  waterMelonArr.append(waterMelon(intArr))

for res in waterMelonArr:
  print(res)

# import math
# print(math.gcd(2,3))
# from itertools import combinations
# print(list(combinations([1,2,3],2)))


# T = int(input())
# gcdArr = []
# def gcd(N,B):
#   A = [idx for idx in range(1,N+1)]
#   from itertools import combinations
#   import math
#   Comb = list(combinations(A,2))
#   newArr = A[:]
#   for singleComb in Comb:
#     g = math.gcd(singleComb[0], singleComb[1])
#     newArr[singleComb[0]-1] = g
#     newArr[singleComb[1]-1] = g
#     if newArr == B:
#       return 'YES'
#     else:
#       newArr = A[:] 
#   return 'NO'

  



# for t in range(T):
#   N = int(input())
#   B = list(map(int,input().split()))
#   gcdArr.append(gcd(N,B))

# for res in gcdArr:
#   print(res)