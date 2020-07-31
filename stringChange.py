word = list(input())
def stringChange(word):
  vowels = ['a', 'e', 'i', 'o', 'u', 'y']
  newString = ""
  for char in word:
    if char.lower() not in vowels:
      newString = "".join([newString, '.', char.lower()])
  return newString

print(stringChange(word))
