arr = list(map(int,input().split()))
k = int(input())
def binarySearch(arr, k):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = low + (high-low)//2
    if arr[mid] == k:
      print(mid)
      break
    elif arr[mid] < k:
      low = mid+1
    else:
      high = mid-1
  return -1
binarySearch(arr,k)