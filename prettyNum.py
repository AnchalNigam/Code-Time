T = int(input())
resArr = []
def prettyNum(numRange):
  prettyNumbers = [2, 3, 9]
  prettyCount = 0
  for num in range(numRange[0], numRange[1]+1):
    strNum = str(num)
    if int(strNum[len(strNum)-1]) in prettyNumbers:
      prettyCount += 1
  return prettyCount



for t in range(T):
  numRange = list(map(int, input().split(' ')))
  resArr.append(prettyNum(numRange))

for res in resArr:
  print(res)
  

