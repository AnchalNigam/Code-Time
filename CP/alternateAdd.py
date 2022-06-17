T = int(input())
result = []
def alternateAdd(A, B):
  diff = B-A
  if diff%3 == 0:
    return 'YES'
  else:
    x = diff//3
    lastNum = x*3
    lastPos = x*2
    if (lastPos+1)%2 != 0:
      lastNum += 1
    else:
      lastNum += 2
    if lastNum == diff:
      return 'YES'
  return 'NO'


for t in range(T):
  A, B = list(map(int,input().split()))
  result.append(alternateAdd(A, B))

for res in result:
  print(res)
