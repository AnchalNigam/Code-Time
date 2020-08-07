T = int(input())
modifiedStringArr = []
def modifyString(string):
  idx = 0
  while idx < len(string):
    if string[idx] == 'b':
      string = string[0:idx] + string[idx+1:]
    elif string[idx:idx+2] == 'ac':
      string = string[0:idx] + string[idx+2:]
    else:
      idx += 1
  return string

for t in range(T):
  string = input()
  modifiedStringArr.append(modifyString(string))

for result in modifiedStringArr:
  print(result)
