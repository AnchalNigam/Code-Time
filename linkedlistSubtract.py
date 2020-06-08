T = input()
def StringShortestDistance(string, char):
  res = []
  for i in range(len(string)):
    if string[i] == char:
      res.append(0)
    else:
      lastIndexChar = string.rindex(char, 0, i)
      lastIndex = string.rindex(string[i], 0, i)
      res.append(abs(lastIndex-lastIndexChar))
  return res

for i in range(int(T)):
  string = input()
  char = input()
  print(StringShortestDistance(string, char))
# StringShortestDistance('anchal', 'a')
