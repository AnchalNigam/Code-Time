strArr = []
for T in range(2):
  strArr.append(input().lower())

def compareString(strArr):
  if strArr[0] < strArr[1]:
    return -1
  elif strArr[0] > strArr[1]:
    return 1
  return 0

print(compareString(strArr))