A = [ 1, 1, 2, 2, 3, 3, 4, 4, 5, 5 ]
A.sort()
print(A)
maxLen = float('-inf')
maxLenCounter = 0
for idx in range(len(A)-1):
  if A[idx]+1 == A[idx+1]:
    maxLenCounter += 1
  elif A[idx] != A[idx+1]:
    if maxLenCounter > maxLen:
      maxLen = maxLenCounter
      print(maxLen)
    maxLenCounter = 0
if maxLenCounter > maxLen:
  maxLen = maxLenCounter

print(maxLen + 1)
                    
