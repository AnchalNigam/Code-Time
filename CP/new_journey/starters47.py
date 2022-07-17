
T = int(input())
result = []
def constructN(n):
  sevenReminder = n%7
  if sevenReminder == 0:
    return 'YES'
  elif sevenReminder%2 == 0:
    return 'YES'
  twoReminder = n%2
  if twoReminder == 0:
    return 'YES'
  elif twoReminder%7 == 0:
    return 'YES'
  return 'NO'

  
for t in range(T):
  N = int(input())
  result.append(constructN(N))

for res in result:
  print(res)