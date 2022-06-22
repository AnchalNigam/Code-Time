# T = int(input())
# result = []
# def chefPoints(X, N):
#   singleCasePoint = X/10
#   return int(singleCasePoint*N)

# for t in range(T):
#   X, N = list(map(int,input().split()))
#   result.append(chefPoints(X, N))

# for res in result:
#   print(res)
# T = int(input())
# result = []
# def whoseChance(P, Q):
#   totalGameFinish = P+Q
#   turnCount = totalGameFinish//2
#   return 'BOB' if (turnCount+1)%2 == 0 else 'ALICE'


# for t in range(T):
#   P, Q = list(map(int,input().split()))
#   result.append(whoseChance(P, Q))

# for res in result:
#   print(res)

# T = int(input())
# result = []
# import math
# def floorsCount(X, Y):
#   chefFloor = math.ceil(X/10)
#   chefinaFloor = math.ceil(Y/10)
#   return abs(chefinaFloor-chefFloor)

# for t in range(T):
#   X, Y = list(map(int,input().split()))
#   result.append(floorsCount(X, Y))

# for res in result:
#   print(res)

T = int(input())
result = []
def formBinary(N):
  odd = "101"
  even = "1001"
  strAddCount = 0
  if N%2 == 0:
    strAddCount = (N-4)//2
    return even + strAddCount*"01"
  else:
    strAddCount = (N-3)//2
    return odd + strAddCount*"01"

for t in range(T):
  N = int(input())
  result.append(formBinary(N))

for res in result:
  print(res)


