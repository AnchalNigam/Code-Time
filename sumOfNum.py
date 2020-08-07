T = int(input())
sumOfDigitsArr = []
def sumOfNumbers(string):
  sumOfDigits = 0
  digitsStr = ""
  for char in string:
    if char.isdigit():
      digitsStr += char
    elif digitsStr != "":
      sumOfDigits += int(digitsStr)
      digitsStr = ""
  if digitsStr != "":
    sumOfDigits += int(digitsStr)
  return sumOfDigits


for t in range(T):
  string = input()
  sumOfDigitsArr.append(sumOfNumbers(string))

for digitsum in sumOfDigitsArr:
  print(digitsum)