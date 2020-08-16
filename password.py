T = int(input())
minPasswordsLens = []
def minPasswordLen(password):
  idx = 0
  while idx < len(password)-1:
    if password[idx] != password[idx+1]:
      password[idx+1] = password[idx]+password[idx+1]
      del password[idx]

    else:
      idx += 1
  idx = len(password)-1
  while idx > 0:
    if password[idx] != password[idx-1]:
      password[idx-1] = password[idx]+password[idx-1]
      del password[idx]
    idx -= 1
    
  return len(password)

for t in range(T):
  passwordSize = int(input())
  password = list(map(int, input().split()))
  minPasswordsLens.append(minPasswordLen(password))

for passwordLen in minPasswordsLens:
  print(passwordLen)