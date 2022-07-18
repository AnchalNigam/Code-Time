T = int(input())
result = []
def isPalin(word):
  charFreq = {}
  for char in word:
    if char not in charFreq:
      charFreq[char] = 1
    else:
      charFreq[char] += 1

  odd = 0
  even = 0
  for _key, value in charFreq.items():
    if value%2 == 0:
      even += 1
    else:
      odd += 1
  if odd > 0:
    return 'NO'
  return 'YES'


for t in range(T):
  N = int(input())
  word = input()
  result.append(isPalin(word))

for res in result:
  print(res)