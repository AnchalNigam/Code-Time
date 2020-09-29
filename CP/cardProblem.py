T = int(input())
finalcardProblemResult = []
def cardProblem(generatedNums):
  chefNumDigit = generatedNums[0]//9
  if generatedNums[0]%9 == 0:
    chefNumDigitLen = chefNumDigit
  else:
    chefNumDigitLen = chefNumDigit+1
  RickNumDigit = generatedNums[1]//9
  if generatedNums[1]%9 == 0:
    RickNumDigitLen = RickNumDigit
  else:
    RickNumDigitLen = RickNumDigit+1
  
  if chefNumDigitLen < RickNumDigitLen:
    return map(str, [0,chefNumDigitLen])
  else:
    return map(str, [1,RickNumDigitLen])

for t in range(T):
  generatedNums = list(map(int,input().split()))
  finalcardProblemResult.append(cardProblem(generatedNums))

for winner in finalcardProblemResult:
  print(' '.join(winner))

