T = int(input())
def sumOfDigits(alphaNumStr):
  digitSum = 0
  for char in alphaNumStr:
    if char.isdigit():
      digitSum += int(char)
  return digitSum


for t in range(T):
  alphaNumStr = input()
  digiSumArr = []
  digiSumArr.append(sumOfDigits(alphaNumStr))

for digiSum in digiSumArr:
  print(digiSum)
