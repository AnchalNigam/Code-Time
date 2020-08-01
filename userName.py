string = list(input())
distinctString = []
for char in string:
  if char not in distinctString:
    distinctString.append(char)

if len(distinctString)%2 != 0:
  print('IGNORE HIM!')
else:
  print('CHAT WITH HER!')
