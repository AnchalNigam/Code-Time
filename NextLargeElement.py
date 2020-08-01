#code
T = int(input())
def nextLargeElement(arr):
    nextLargeElemArr = []
    for idx1 in range(len(arr)):
        flag = False
        for idx2 in range(idx1+1, len(arr)):
            if arr[idx2] > arr[idx1]:
                flag = True
                nextLargeElemArr.append(str(arr[idx2]))
                break
        if flag == False:
            nextLargeElemArr.append('-1')
    return nextLargeElemArr
        
for t in range(T):
    sizeOfArr = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    nextLargeElemFinalArr = []
    nextLargeElemFinalArr.append(nextLargeElement(arr))
    
for nextLargeElems in nextLargeElemFinalArr:
    print(' '.join(nextLargeElems))
    