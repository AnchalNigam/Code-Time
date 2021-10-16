def binarySearch(arr, start, end, k):
  low = start
  high = end
  while low <= high:
    mid = low + (high-low)//2
    if arr[mid] == k:
      return mid
    elif arr[mid] < k:
      low = mid+1
    else:
      high = mid-1
def findIndices(A, k):
  high = 1
  low = 0
  while A[high] < k:
    low = high
    high *= 2

  return binarySearch(A, low, high, k)
A = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
print(findIndices(A, 10))

# find element in infinite sorted array. first task is to find low and high
#  for that we first take high = 1 then comparison of high with key because normally high
# greater than search element so once we find high greater than search mns inside low and
# high search elem would be present. for optimization start we also make previous high
