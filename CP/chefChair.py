T = int(input())
result = []
def minimumChairReq(X, Y):
  if Y > X:
    return 0
  else:
    return X - Y

for t in range(T):
  X, Y = list(map(int,input().split()))
  result.append(minimumChairReq(X, Y))

for res in result:
  print(res)
