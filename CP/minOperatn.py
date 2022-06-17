T = int(input())
result = []
import math
def minOperatn(x, y):
  if x == y:
    return x
  else:
    if x > y:
      x, y = y, x 
    if y == 0 or x == 0 or y%x != 0:
      return -1
    n = (math.log2(y/x))+1
    if (n - int(n)) == 0:
      return int(n-1) + y 
  return -1



for t in range(T):
  X, Y = list(map(int,input().split()))
  result.append(minOperatn(X, Y))

for res in result:
  print(res)
