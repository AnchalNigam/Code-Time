T = int(input())
subStringIndexs = []
def implementStr(string1, string2):
  for idx in range(len(string1)):
    if string1[idx:idx+len(string2)] == string2:
      return idx
  return -1


for t in range(T):
  string1 = input()
  string2 = input()
  subStringIndexs.append(implementStr(string1, string2))

for index in subStringIndexs:
  print(index)