def binarySearch(arr, left, right, searchKey):
  if(left > right ):
    return -1
  
  mid = (left + right)//2
  if (arr[mid] == searchKey):
    return mid
  if(arr[mid] < searchKey):
    return binarySearch(arr, mid+1, right, searchKey)
  
  return binarySearch(arr, left, mid-1, searchKey)

print(binarySearch([2,5,8,10], 0, 3, 11))
