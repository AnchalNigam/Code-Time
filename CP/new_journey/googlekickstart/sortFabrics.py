T = int(input())
def sortFabrics(N, arr):
  arr1 = sorted(arr)
  arr.sort(key = lambda x: (x[1], x[2]))
  count = 0
  for i in range(N):
    if arr1[i][2] == arr[i][2]:
      count += 1
  return count




for t in range(T):
  N = int(input())
  arr = []
  for i in range(N):
    x = input().split()
    x[1] = int(x[1])
    x[2] = int(x[2])
    arr.append(x)
  print(f"Case #{t+1}: {sortFabrics(N, arr)}")