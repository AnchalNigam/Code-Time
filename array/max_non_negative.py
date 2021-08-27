def maxset(A):
    summation = 0
    maxSum = float('-inf')
    maxIdx = -1
    minIdx = -1
    minIdxTemp = -1
    for idx in range(len(A)):
        if(A[idx] > -1):
            summation += A[idx]
            if summation > maxSum:
              maxIdx = idx
              maxSum = summation
              minIdx = minIdxTemp
           
            elif summation == maxSum:
              if minIdx == -1 and maxIdx <= (idx-(minIdxTemp+1)) or (minIdx != -1 and (maxIdx-minIdx) <= (idx-(minIdxTemp+1))):
                maxIdx = idx
                minIdx = minIdxTemp
                maxSum = summation
        else:
            summation = 0
            minIdxTemp = idx
    result = []
    for idx in range(minIdx+1, maxIdx+1):
        result.append(A[idx])
    return result

print(maxset([9,0,0,0, -9,2,3,4,-8]))
