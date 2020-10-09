alexStone = 0
leeStone = 0
piles = [3,7,2,3]
count = 0
while len(piles) != 0:
  maxNum = max(piles[0], piles[len(piles)-1])
  if len(piles) %2 == 0:
    alexStone += maxNum
  else:
    leeStone += maxNum
  print(piles)
  piles.remove(maxNum)
if alexStone > leeStone:
  print(True)
print(False)
    