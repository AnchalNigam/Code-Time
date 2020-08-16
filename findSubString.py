T = int(input())
findSubStringArr = []
def findSubstring(string, subString):
  copySubString = list(subString)
  idx = 0
  while idx < len(string):
    if len(copySubString) == 0:
      break
    if string[idx] in copySubString:
      del copySubString[copySubString.index(string[idx])]
      string = string[0:idx] + string[idx+1:len(string)]
    else:
      idx+=1
    
  sortedString = sorted(string+subString[0])
  string = ''.join(sortedString)
  findFirstCharIndexOfSubString = string.rindex(subString[0])
  finalString = string[0:findFirstCharIndexOfSubString]+subString+string[findFirstCharIndexOfSubString+1:]

  return finalString



for t in range(T):
  string = input()
  subString = input()
  findSubStringArr.append(findSubstring(string, subString))

for string in findSubStringArr:
  print(string)

