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


# why low+high/2 not because every integer type is having some holding capacity so if high
# is more then overflow occurs that your integrer does not hold and give unexpected result