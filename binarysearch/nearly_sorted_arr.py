def nearlySortedArr(A, k):
  low = 0
  high = len(A) - 1
  while low <= high:
    mid = low + (high-low)//2
    if A[mid] == k:
      return mid
    elif mid > low and A[mid-1] == k:
      return mid-1 
    elif mid < high and A[mid+1] == k:
      return mid+1
    elif A[mid] < k:
      low = mid + 1
    elif A[mid] > k:
      high = mid - 1
  return -1

A = [10, 3, 40, 20, 50, 80, 70]
print(nearlySortedArr(A, 40))

# in this way basically one element is either at x-1 or x+1 or x.
# in this, we first check mid and mid -1 and mid+1 and also make sure, mid should
# not dec than left and more than right
# and then normal binary search