T = input()
def lastIndex(inputStr):
  lastIdxVal = -1
  for idx in range(len(inputStr)):
    if inputStr[idx] == '1':
      lastIdxVal = idx
  return lastIdxVal
 


for i in range(int(T)):
  arr = input()
  print(lastIndex(arr))