T = int(input())
giftFixArr = []
def giftFix(candyArr, orangeArr):
  smallestCandy = sorted(candyArr)[0]
  smallestOrange = sorted(orangeArr)[0]
  candyResArr = []
  orangeResArr = []
  for idx in range(len(candyArr)):
    candyResArr.append(candyArr[idx]-smallestCandy)
    orangeResArr.append(orangeArr[idx]-smallestOrange)
  movesCount = 0
  print(candyResArr, orangeResArr, 'check')
  for idx2 in range(len(candyResArr)):
    if smallestCandy > smallestOrange:
      if candyResArr[idx2] > orangeResArr[idx2] and orangeResArr[idx2] != 0:
        movesCount += candyResArr[idx2] + 1
      else:
        movesCount += candyResArr[idx2]
    else:
      if orangeResArr[idx2] > candyResArr[idx2] and candyResArr[idx2] != 0:
        movesCount += orangeResArr[idx2] + 1
      else:
        movesCount += orangeResArr[idx2]

  return movesCount


  

for t in range(T):
  size = int(input())
  candyArr = list(map(int, input().split()))
  orangeArr = list(map(int, input().split()))
  giftFixArr.append(giftFix(candyArr, orangeArr))

for result in giftFixArr:
  print(result)