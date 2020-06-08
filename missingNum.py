T = input()
def missingNum(arr, n):
  expectedSum = int(n*((n+1)/2))
  originalSum = sum(arr)
  return expectedSum-originalSum


for i in range(int(T)):
  sizeArr = int(input())
  arr = input().split()
  arr = list(map(int, arr))
  print(missingNum(arr, sizeArr))
