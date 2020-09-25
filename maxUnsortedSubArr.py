def subUnsort(A):

  smallestIdx = float('-inf')
  for idx in range(len(A)-1):
    if A[idx] > A[idx+1]:
      smallestIdx = idx
      break
  largestIdx = float('inf')
  for idx in range(len(A)-1,0,-1):
    if A[idx-1] > A[idx]:
      largestIdx = idx
      break
  
  if smallestIdx == float('-inf') and largestIdx == float('inf'):
    return [-1]
  maxiumSub = max(A[smallestIdx:largestIdx+1])
  minimumSub = min(A[smallestIdx:largestIdx+1])
  for idx in range(0, smallestIdx):
    if A[idx] > minimumSub:
      smallestIdx = idx
      break

  for idx in range(len(A)-1, largestIdx, -1):
    if A[idx] < maxiumSub:
      largestIdx = idx
      break

  return [smallestIdx, largestIdx]

print(subUnsort([ 1,3,2 ]
))




