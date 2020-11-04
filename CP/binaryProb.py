# def maximumPower(s):
#   # Write your code here
#   if len(s) > 10**2:
#     return -1
#   idx = len(s) -1
#   oneIdxArr = []
#   while idx >= 0:
#     if s[idx] == '1':
#       oneIdxArr.append(len(s)-1-idx)
#     idx -= 1
#   if len(oneIdxArr) == 0:
#     return 0
#   # if oneIdxArr[len(oneIdxArr)-1] != len(s)-1: 
#   for idx in range(len(oneIdxArr)):
#     oneIdxArr[idx] = len(s)-1-oneIdxArr[idx]
#   decimalNum = 0
#   for value in oneIdxArr:
#     decimalNum += 2**value
#   cnt = 0
#   print(decimalNum)
#   while decimalNum % 2 == 0: 
#     cnt = cnt + 1
#     decimalNum = int(decimalNum // 2) 
#   return cnt
# print(maximumPower('1001'))
# def maximumPower(s):
#   # Write your code here
#   idx = len(s) -1
#   oneIdxArr = []
#   while idx >= 0:
#     if s[idx] == '1':
#       oneIdxArr.append(len(s)-1-idx)
#     idx -= 1
#   if len(oneIdxArr) == 0:
#     return 0
#   rounds = 0
#   roundIdx = 0
#   for idx in range(len(oneIdxArr)-1):
#     if oneIdxArr[idx]+1 != oneIdxArr[idx+1]:
#       rounds = idx + 1
#       roundIdx = idx
#       break
#   if len(oneIdxArr) == 2 and oneIdxArr[0]+1 == oneIdxArr[1]:
#     rounds = 2
#     roundIdx = 1
#   if rounds == 1 and oneIdxArr[0] == 0:
#     oneIdxArr[0] = len(s)-1
#     for idx in range(1, len(oneIdxArr)):
#       oneIdxArr[idx] = oneIdxArr[idx] - rounds
#   else:
#     for idx in range(roundIdx+1):
#       oneIdxArr[idx] = oneIdxArr[idx] + rounds
#     for idx in range(roundIdx+1, len(oneIdxArr)):
#       oneIdxArr[idx] = oneIdxArr[idx] - rounds

#   decimalNum = 0
#   for value in oneIdxArr:
#     decimalNum += 2**value
#   print(decimalNum)
#   cnt = 0
#   while decimalNum % 2 == 0: 
#     cnt = cnt + 1
#     decimalNum = int(decimalNum // 2) 
#   return cnt
# print(maximumPower('1011010'))
def maximumPower(s):
  idx = len(s) -1
  oneIdxArr = []
  dubOneIdxArr = []
  maxCnt = float('-inf')
  while idx >= 0:
    if s[idx] == '1':
      oneIdxArr.append(len(s)-1-idx)
      dubOneIdxArr.append(len(s)-1-idx)
    idx -= 1
  if len(oneIdxArr) == 0:
    return 0
  while True:
    for idx in range(len(dubOneIdxArr)):
      if dubOneIdxArr[idx] - 1 < 0:
        dubOneIdxArr[idx] = len(s)-1
      else:
        dubOneIdxArr[idx] -= 1
    if ''.join(map(str, dubOneIdxArr)) == ''.join(map(str, oneIdxArr)):
      break
    decimalNum = 0
    for value in dubOneIdxArr:
      decimalNum += 2**value
    cnt = 0
    while decimalNum % 2 == 0: 
      cnt = cnt + 1
      decimalNum = int(decimalNum // 2) 
    if maxCnt < cnt:
      maxCnt = cnt
  return maxCnt
print(maximumPower('0011'))
      
        

  
