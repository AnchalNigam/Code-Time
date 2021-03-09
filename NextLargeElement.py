#code
T = int(input())
nextLargeElemFinalArr = []

# def nextLargeElement(arr):
#     nextLargeElemArr = []
#     for idx1 in range(len(arr)):
#         flag = False
#         for idx2 in range(idx1+1, len(arr)):
#             if arr[idx2] > arr[idx1]:
#                 flag = True
#                 nextLargeElemArr.append(str(arr[idx2]))
#                 break
#         if flag == False:
#             nextLargeElemArr.append('-1')
#     return nextLargeElemArr
        
def nextLargeElement(arr):
    nextLargeElemArr = ['-1'] * len(arr)
    stack = []
    stack.append(0)
    for idx in range(1, len(arr)):
      poppedIdx = stack.pop()
      while(arr[idx] > arr[poppedIdx]):
        nextLargeElemArr[poppedIdx] = str(arr[idx])
        if len(stack) == 0:
          break
        poppedIdx = stack.pop()
      if arr[idx] < arr[poppedIdx]:
        stack.append(poppedIdx)
      stack.append(idx)
    return nextLargeElemArr

       

for t in range(T):
    sizeOfArr = int(input())
    arr = list(map(int, input().split()))
    nextLargeElemFinalArr.append(nextLargeElement(arr))
    
for nextLargeElems in nextLargeElemFinalArr:
    print(' '.join(nextLargeElems))

# 2nd way
const stack = []
const G = [];
for(let idx = n-1; idx >= 0; idx--) {
  while(stack.length > 0 && stack[stack.length-1] <= arr[idx]) {
    stack.pop();
  }
  
  if(stack.length === 0) {
    G.unshift(-1);
  } else {
    G.unshift(stack[stack.length-1]);
  }
  
  stack.push(arr[idx]);
}
return G;

    