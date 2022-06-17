T = int(input())
result = []
def equalStr(n, str1, str2):
  c = 0
  replacedChar = {}
  for i in range(n):
    if str1[i] != str2[i]:
      if str2[i] not in replacedChar:
        replacedChar[str2[i]] = 1
        c += 1
  return c
for t in range(T):
  n = int(input())
  str1 = input().strip()
  str2 = input().strip()
  result.append(equalStr(n, str1, str2))

for res in result:
  print(res)
