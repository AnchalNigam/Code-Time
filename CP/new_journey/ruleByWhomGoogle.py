
def findTheKingdomRuler(kingdomName):
  vowels = {
    'a': 'a',
    'e': 'e',
    'i': 'i',
    'o': 'o',
    'u': 'u'
  }

  lastChar = kingdomName[len(kingdomName)-1].lower()
  print(lastChar, 'last')
  if lastChar == 'y':
    return 'nobody'
  elif lastChar in vowels:
    return 'Alice'
  return 'Bob'
  
numOfCases = int(input())
for cases in range(numOfCases):
  kingdomName = input()
  ruler = findTheKingdomRuler(kingdomName)
  print(f"Case #{cases+1}: {kingdomName} is ruled by {ruler}")

