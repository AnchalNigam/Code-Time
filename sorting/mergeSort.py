arr = [4, 2, 5, 1, 9, 10, 0, 12, 11]
def mergeArr(arr, L, R):
  i=j=k=0
  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
  while i < len(L):
    arr[k] = L[i]
    i += 1
    k += 1
  while j < len(R):
    arr[k] = R[j]
    j += 1
    k += 1
  
def mergeSort(arr):
  if(len(arr) != 1):
    mid = (0+len(arr))//2
    L = arr[0:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    mergeArr(arr, L, R)
  return arr
print(mergeSort(arr))
