

from re import L


T = int(input())
def curling(Rs, Rh, N, M, red, yellow):
  # print(red, yellow)
  validRed = []
  validYellow = []
 
  import math
  for i in range(N):
    dist = math.sqrt(((red[i][0])**2)+((red[i][1])**2))
    actualDist = dist-Rs
    if actualDist <= Rh:
      validRed.append(dist)
  for i in range(M):
    dist = math.sqrt(((yellow[i][0])**2)+((yellow[i][1])**2))
    actualDist = dist-Rs
    if actualDist <= Rh:
      validYellow.append(dist)   
  validRed.sort()
  validYellow.sort()
  vN = len(validRed)
  vM = len(validYellow)
  redPoint, yellowPoint = 0, 0
  i, j = 0, 0 
  # print(validRed, validYellow, 'lllllllllllllll', i, j)
  if not vN or not vM:
    return [vN, vM]

  while i < vN and j < vM:
    if validRed[i] <= validYellow[j]:
      redPoint += 1
      i += 1
    else:
      break
  i, j = 0, 0
  while i < vM and j < vN:
    # print(validYellow[i], validRed[j], '(((((((((((')
    if validYellow[i] <= validRed[j]:
      yellowPoint += 1
      i += 1
    else:
      break
  if redPoint > yellowPoint:
    return [redPoint, 0]
  elif redPoint == yellowPoint:
    return [0,0]
  else:
    return [0, yellowPoint]
  
  



for t in range(T):
  Rs, Rh = list(map(int, input().split()))
  N = int(input())
  red = []
  yellow = []
  for i in range(N):
    x = list(map(int, input().split()))
    red.append(x)
  M = int(input())
  for j in range(M):
    x = list(map(int, input().split()))
    yellow.append(x)
  
  print(f"Case #{t+1}: {' '.join(map(str, curling(Rs, Rh, N, M, red, yellow)))}")