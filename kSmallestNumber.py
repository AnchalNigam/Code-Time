T = input()
def kSmallestNum(arr, k):
  arr.sort()
  return arr[k-1]

for i in range(int(T)):
  sizeArr = int(input())
  arr = input().split()
  k = int(input())
  arr = list(map(int, arr))
  print(kSmallestNum(arr, k))
