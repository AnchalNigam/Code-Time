T = int(input())
minEnergyArr = []
def minEnergy(numArr):
  minimumEnergy = 0
  newMinEnergy = minimumEnergy
  sumOfNum = 0
  for num in numArr:
    sumOfNum += num
    if sumOfNum <= 0:
      newMinEnergy = abs(sumOfNum-1)
    if newMinEnergy > minimumEnergy:
      minimumEnergy = newMinEnergy
  if minimumEnergy == 0:
    return 1
  return minimumEnergy

for t in range(T):
  size = int(input())
  numArr = list(map(int, input().split()))
  minEnergyArr.append(minEnergy(numArr))

for result in minEnergyArr:
  print(result)
