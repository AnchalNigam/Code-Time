def maximumPower(s):
  # Write your code here
  if len(s) > 10**2:
    return -1
  idx = len(s) -1
  oneIdxArr = []
  while idx >= 0:
    if s[idx] == '1':
      oneIdxArr.append(len(s)-1-idx)
    idx -= 1
  if len(oneIdxArr) == 0:
    return 0
  for idx in range(len(oneIdxArr)):
    oneIdxArr[idx] = len(s)-1-idx

  decimalNum = 0
  for value in oneIdxArr:
    decimalNum += 2**value
  cnt = 0
  print(decimalNum)
  while decimalNum % 2 == 0: 
    cnt = cnt + 1
    decimalNum = int(decimalNum // 2) 
  return cnt
print(maximumPower('111'))