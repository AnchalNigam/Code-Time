T = input()
def slideWindow(arr,k):
  window_sum = sum([arr[i] for i in range(k)])
  n = len(arr)
  for i in range(n-k):
    new_window_sum = window_sum - arr[i] + arr[i+k]
    if new_window_sum > window_sum:
      window_sum = new_window_sum
  return window_sum

for i in range(int(T)):
  k = int(input())
  arr = list(map(int,input().split()))
  print(slideWindow(arr,k))