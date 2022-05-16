def findRotationPoint(nums):
  low = 0
  high = len(nums)-1
  while low < high:
    mid = low + ((high-low)//2)
    # print(mid, 'mid')
    if nums[mid] < nums[high]:
      high = mid
    else:
      low = mid+1
  return low

nums = [1, 3, 8, 10]
print(findRotationPoint(nums))

# above approach is of pepcoding where smallest elem index is returned which intrun telling no of rotation
# below approach is grokking sol
def count_rotations(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2

    # if mid is greater than the next element
    if mid < end and arr[mid] > arr[mid + 1]:
      return mid + 1

    # if mid is smaller than the previous element
    if mid > start and arr[mid - 1] > arr[mid]:
      return mid

    if arr[start] < arr[mid]:  # left side is sorted, so the pivot is on right side
      start = mid + 1
    else:  # right side is sorted, so the pivot is on the left side
      end = mid - 1

  return 0  # the array has not been rotated
