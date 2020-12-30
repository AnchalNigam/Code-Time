rowsCol = list(map(int,input().split()))
codingBelt2DArr = []
codingBeltMaxCoders = []
def findCodingBeltMaxCoders(codingBelt2DArr, rows, cols):
  codingBelt2DArrConnectionInfo = [row[:] for row in codingBelt2DArr]
  for i in range(rows):
    for j in range(cols):
      count = 0
      if codingBelt2DArr[i][j] == 1:
        if i-1 >= 0 and codingBelt2DArr[i-1][j] == 1:
          count += 1
        if i+1 < rows and codingBelt2DArr[i+1][j] == 1:
          count += 1
        if j-1 >= 0 and codingBelt2DArr[i][j-1] == 1:
          count += 1
        if j+1 < cols and codingBelt2DArr[i][j+1] == 1:
          count += 1
      codingBelt2DArrConnectionInfo[i][j] = count
  maxCodersInCodingBelt = 0
  for i in range(rows):
    for j in range(cols):
      if codingBelt2DArrConnectionInfo[i][j] >= 1:
        if i-1 >= 0 and codingBelt2DArrConnectionInfo[i-1][j] + codingBelt2DArrConnectionInfo[i][j] >= maxCodersInCodingBelt:
          maxCodersInCodingBelt = codingBelt2DArrConnectionInfo[i-1][j] + codingBelt2DArrConnectionInfo[i][j]
        if i+1 < rows and codingBelt2DArrConnectionInfo[i+1][j] + codingBelt2DArrConnectionInfo[i][j] >= maxCodersInCodingBelt:
          maxCodersInCodingBelt = codingBelt2DArrConnectionInfo[i+1][j] + codingBelt2DArrConnectionInfo[i][j]
        if j-1 >= 0 and codingBelt2DArrConnectionInfo[i][j-1] + codingBelt2DArrConnectionInfo[i][j] >= maxCodersInCodingBelt:
          maxCodersInCodingBelt = codingBelt2DArrConnectionInfo[i][j-1] + codingBelt2DArrConnectionInfo[i][j]
        if j+1 < cols and codingBelt2DArrConnectionInfo[i][j+1] + codingBelt2DArrConnectionInfo[i][j] >= maxCodersInCodingBelt:
          maxCodersInCodingBelt = codingBelt2DArrConnectionInfo[i][j+1] + codingBelt2DArrConnectionInfo[i][j]
  return maxCodersInCodingBelt


for row in range(rowsCol[0]):
  codingBelt2DArr.append(list(map(int,input().split())))

print(findCodingBeltMaxCoders(codingBelt2DArr, rowsCol[0], rowsCol[1]))

# for cardsNum in pokemonCardsAtDthDay:
#   print(cardsNum)

