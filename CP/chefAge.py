# T = int(input())
# result = []
# def equalDistribution(inputs):
#   totalChoco = inputs[0] + inputs[1]
#   return 'YES' if totalChoco % 2 == 0 else 'NO'

# for t in range(T):
#   inputs = list(map(int,input().split()))
#   result.append(equalDistribution(inputs))

# for res in result:
#   print(res)

# T = int(input())
# result = []
# def minPoints(X, Y):
#   return 7-max(X,Y)


# for t in range(T):
#   X, Y = list(map(int,input().split()))
#   result.append(minPoints(X, Y))

# for res in result:
#   print(res)
# T = int(input())
# result = []
# def isValidCoordinate(X, Y):
#   if 1 <= X <= 8 and 1 <= Y <= 8:
#     return True 
#   return False
# def canKnightAttack(X, Y):
#   X1, Y1 = X
#   X2, Y2 = Y
#   XPos = {}
#   XPos[(X1+2, Y1+1)] = 1
#   XPos[(X1+2, Y1-1)] = 1
#   XPos[(X1+1, Y1+2)] = 1
#   XPos[(X1+1, Y1-2)] = 1
#   XPos[(X1-2, Y1+1)] = 1
#   XPos[(X1-2, Y1-1)] = 1
#   XPos[(X1-1, Y1+2)] = 1
#   XPos[(X1-1, Y1-2)] = 1

#   for pos in list(XPos.keys()):
#     if(not isValidCoordinate(pos[0], pos[1])):
#       del XPos[pos]
#   for i in range(8):
#     co = (X2,Y2)
#     if i == 0:
#       co = (X2+2, Y2+1)
#     elif i == 1:
#       co = (X2+2, Y2-1)
#     elif i == 2:
#       co = (X2+1, Y2+2)
#     elif i == 3:
#       co = (X2+1, Y2-2)
#     elif i == 4:
#       co = (X2-2, Y2+1)
#     elif i == 5:
#       co = (X2-2, Y2-1)
#     elif i == 6:
#       co = (X2-1, Y2+2)
#     elif i == 7:
#       co = (X2-1, Y2-2)
#     if co in XPos:
#       return  'YES'
#   return 'NO'
  
# for t in range(T):
#   X1, Y1 = list(map(int,input().split()))
#   X2, Y2 = list(map(int,input().split()))

#   result.append(canKnightAttack((X1, Y1), (X2, Y2)))

# for res in result:
#   print(res)

from telnetlib import X3PAD


T = int(input())
result = []
mod = (1000000007)
def calorieBurn(N, X):
  dp = [0]*(N+1)
  dp[1] = X
  summation = X
  summation1 = X
  for i in range(2, N+1):
    summation1 = ((summation) +(dp[i-1]))
    # summation = ((summation%mod) +(dp[i-1]%mod))%mod
    dp[i] = summation1
    summation = (summation + summation1)
  return dp[N]%mod

for t in range(T):
  N, X = list(map(int,input().split()))
  result.append(calorieBurn(N, X))

for res in result:
  print(res)