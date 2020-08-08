T = int(input())
countArr = []
def countOccurenceAnagrams(string1, string2):
  reverseString2 = string2[::-1]
  string2Len = len(string2)
  string2 = ''.join(sorted(string2))
  countOccurence = 0
  idx = 0 
  while idx <= len(string1)-len(string2):
    if  ''.join(sorted(string1[idx:idx+string2Len])) == string2:
      countOccurence += 1
    idx += 1
  return countOccurence


for t in range(T):
  string1 = input()
  string2 = input()
  countArr.append(countOccurenceAnagrams(string1, string2))

for result in countArr:
  print(result)
