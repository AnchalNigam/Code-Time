T = int(input())
smallFirstLastCharCounts = []
def sameFirstLastChar(string):
  dic = {}
  count = len(string)
  for idx in range(len(string)):
    if string[idx] not in dic:
      dic[string[idx]] = [idx]
    else:
      dic[string[idx]].append(idx)
  for key in list(dic.keys()):
    keyValueLen = len(dic[key])-1
    count += (keyValueLen*(keyValueLen+1)/2)
  
  return int(count)

  

for t in range(T):
  size = int(input())
  string = input()
  smallFirstLastCharCounts.append(sameFirstLastChar(string))

for count in smallFirstLastCharCounts:
  print(count)