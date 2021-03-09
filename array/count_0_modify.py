change = 0
maxCount = 0
count = 0
lastIdx = 0
A =  [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ]
B =  2
for idx in range(len(A)):
  if A[idx] == 1:
    count += 1
  elif A[idx] == 0 and change < B:
    count += 1
    change += 1
    lastIdx = idx
  elif change >= B:
    maxCount = max(maxCount, count)
    print(maxCount)
    change = 1
    count = idx - lastIdx
    lastIdx = idx
maxCount = max(maxCount, count)
print(maxCount+B-1)
  
