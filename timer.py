T = input()
def spies(arr):
  numOfSpies = 0
  print(arr)
  for i in range(len(arr)):
    j = 0
    while j <= len(arr) - 3:
      if ((arr[i][j] == "." and arr[i][j+1] == "." and arr[i][j+2] == ".") or (arr[i][j] != "." and arr[i][j+1] != "." and arr[i][j+2] != ".")):
        numOfSpies += 1
        j += 3
      else:
        j += 1
  for i in range(len(arr)):
    j = 0
    while j <= len(arr) - 3:
      if ((arr[j][i] == "." and arr[j+1][i] == "." and arr[j+2][i] == ".") or (arr[j][i] != "." and arr[j+1][i] != "." and arr[j+2][i] != ".")):
        numOfSpies += 1
        j += 3
      else:
        j += 1
  for i in range(len(arr)):
    j = 0
    while j <= len(arr) - 3:
      if ((arr[j][j] == "." and arr[j+1][j+1] == "." and arr[j+2][j+2] == ".") or (arr[j][j] != "." and arr[j+1][j+1] != "." and arr[j+2][j+2] != ".")):
        numOfSpies += 1
        j += 3
      else:
        j += 1
  return numOfSpies


for i in range(int(T)):
  k = int(input())
  finalArr = []
  for j in range(k):
    arr = input().split()
    finalArr.append(arr)
  print(spies(finalArr))