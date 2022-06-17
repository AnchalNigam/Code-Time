T = int(input())
result = []
import math
def minTVSubscribe(n, cost):
  groups = math.ceil(n/6)
  return groups * cost

for t in range(T):
  n, cost = list(map(int,input().split()))
  result.append(minTVSubscribe(n, cost))

for res in result:
  print(res)
