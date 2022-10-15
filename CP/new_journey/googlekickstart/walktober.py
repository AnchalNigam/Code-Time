

T = int(input())
def minSteps(M, N, arr, P):
  result = [[0 for i in range(M)] for j in range(N)]
  for i in range(M):
    for j in range(N):
      result[j][i] = arr[i][j]
  minSteps = 0
  for i in range(N):
    maxSteps = max(result[i])
    minSteps += (maxSteps-result[i][P-1])
  return minSteps




for t in range(T):
  M, N, P = list(map(int, input().split()))
  arr = []
  for i in range(M):
    x = list(map(int, input().split()))
    arr.append(x)
  print(f"Case #{t+1}: {minSteps(M, N, arr, P)}")