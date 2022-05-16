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


# ans why we cant inc it in 10 20 times
# if we increase it by 10 times or 20 times, then we will definitely reach the binary space very quickly. 
# For example, if we have to search for 11,000 in Natural numbers set, then we will reach the binary space [10,000 to 1,00,000] very quickly, but the time taken to search within the binary space increases too. Instead, if we just double every time, then our binary space remains small, but we take more time to reach that space.
# So, it's just a tradeoff as @Aditya Verma said.

#  Number of steps for finding high index ‘h’ is O(Log p). 
# ans lies betwen l and h.suppose p elements are there then log(p)