T = int(input())
result = []
def consistencyChangeCount(s):
  vowels = {
    'A': 'A',
    'E': 'E',
    'I': 'I',
    'O': 'O',
    'U': 'U'
  }

  constFreq = {}
  constMaxCount = 0
  vowelsMaxCount = 0
  vowelsFreq = {}
  vowelsCount = 0
  constCount = 0
  for char in s:
    if char in vowels:
      vowelsCount += 1
      if char not in vowelsFreq:
        vowelsFreq[char] = 1
      else:
        vowelsFreq[char] += 1
      vowelsMaxCount = max(vowelsMaxCount, vowelsFreq[char])
    else:
      constCount += 1
      if char not in constFreq:
        constFreq[char] = 1
      else:
        constFreq[char] += 1
      constMaxCount = max(constMaxCount,  constFreq[char])
  x = vowelsCount + (constCount-constMaxCount)*2
  y = constCount + (vowelsCount-vowelsMaxCount)*2
  return min(x, y)





for t in range(T):
  s = input()
  op = consistencyChangeCount(s)
  result.append(op)
  # print(f"Case #{t+1}: {op}")
for i in range(len(result)):
  print(f"Case #{i+1}: {result[i]}")