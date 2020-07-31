N = int(input())
wordsArr = []
for T in range(N):
  wordsArr.append(input())
def shortTooLongWords(wordsArr):
  for idx in range(len(wordsArr)):
    wordLen = len(wordsArr[idx])
    if wordLen > 10:
      newWord = wordsArr[idx][0] + str((wordLen - 2)) + wordsArr[idx][wordLen-1]
      wordsArr[idx] = newWord
  return wordsArr

newWordsArr = shortTooLongWords(wordsArr)

for newWord in newWordsArr:
  print(newWord)

