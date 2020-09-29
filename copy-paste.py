T = int(input())
copyPasteArr = []
def copyPaste(intArr, n, k):
  a = intArr
  arr = [idx for idx in range(len(intArr))]
  from itertools import combinations
  c = list(combinations(arr,2))
  moves = 0
  counter = 0
  maxVal = (float('inf'), 0)
  while True:
    flag = False
    maxVal = (float('inf'), 0)
    for idx in range(len(c)):
      print(a[c[idx][0]] + a[c[idx][1]], idx, maxVal[0], 'check')
      if a[c[idx][0]] + a[c[idx][1]] <= k and maxVal[0] >= (a[c[idx][0]] + a[c[idx][1]]):
        print('check', a[c[idx][0]] + a[c[idx][1]] )
        flag = True
        maxVal = (a[c[idx][0]] + a[c[idx][1]],min(c[idx]))
      # else:
      #   flag = True
    if flag == True:
      a[maxVal[1]] = maxVal[0]
      moves += 1
      print('chekingg')
      # break
    else:
      break
    # counter += 1
    # if counter == 2:
    #   break
    print(a)
  return moves
 
for t in range(T):
  initailArr = list(map(int,input().split()))
  intArr = list(map(int,input().split()))
  copyPasteArr.append(copyPaste(intArr, initailArr[0], initailArr[1]))

for res in copyPasteArr:
  print(res)