T = int(input())
covidRunStatus = []
# 12 3 4 2
def covidRun(covidRunData):
  # x = covidRunData[2]
  # roundNum = 0
  # isSecondIteration = False
  # while roundNum == 0:
  #   c = (x+covidRunData[1])%covidRunData[0]
  #   # isSecondIteration = (x+covidRunData[1])//covidRunData[0] != 0
  #   if (x+covidRunData[1])//covidRunData[0] != 0:
  #     isSecondIteration = True
  #   if c == covidRunData[3]:
  #     return 'YES'
  #   x = c
  #   if x >= covidRunData[2] and isSecondIteration:
  #     roundNum += 1
  #   # if count > 6:
  #   #   break
  # return 'NO'
  # if covidRunData[1] % 2 != 0:
  #   return 'YES'

  # if covidRunData[1] % 2 == 0:
  #   if covidRunData[2]%2 != 0:
  #     if covidRunData[0]%2 != 0:
  #       return 'YES'
  #     else:
  #       if covidRunData[3]%2 == 0:
  #         return 'NO'
  #       else:
  #         return 'YES'
  #   else:
  #     if covidRunData[0]%2 == 0:
  #       if covidRunData[3]%2 == 0:
  #         return 'YES'
  #       else:
  #         return 'NO'
  #     else:
  #       return 'YES'
  # if covidRunData[1] == 0 or covidRunData[2] == 0:
  #   return 'NO'
  # element1 = covidRunData[0] + covidRunData[3]
  # element2 = covidRunData[0] + element1
  # # element = covidRunData[2] + (n-1)covidRunData[1]
  # # element = covidRunData[2] + n*covidRunData[1] - covidRunData[1]
  # # element = covidRunData[2] - covidRunData[1] + n*covidRunData[1]
  # n1 = (element1 - covidRunData[2] + covidRunData[1])%covidRunData[1]
  # if n1 == 0:
  #   return 'YES'
  # else:
  #   n2 = (element2 - covidRunData[2] + covidRunData[1])%covidRunData[1]
  #   if n2 == 0:
  #     return 'YES'
  # return 'NO'
  arr = []
  count = 0
  x = covidRunData[2]
  while True:
    # count += 1
    x = x+covidRunData[1]
    if x%covidRunData[0] in arr:
      break
    else:
      arr.append(x%covidRunData[0])
    # if count >= 11:
    #   break
  # print(arr)
  if covidRunData[3] in arr:
    return 'YES'
  return 'NO'
    



for t in range(T):
  covidRunData = list(map(int,input().split()))
  covidRunStatus.append(covidRun(covidRunData))

for result in covidRunStatus:
  print(result)

