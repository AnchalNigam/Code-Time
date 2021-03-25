arr = list(map(int, input().split()))
stack = []
res = [-1]*len(arr)
for idx in range(len(arr)):
  while len(stack) != 0:
    if stack[len(stack)-1] < arr[idx]:
      res[idx] = stack[len(stack)-1]
      break

    else:
      stack.pop()

  stack.append(arr[idx])

print(res)
# other way
def prevSmaller(self, A):
      stack = []
      result = [-1 for idx in range(len(A))]
      if len(A) == 0:
          return result
      stack.append(A[0])
      for idx in range(1, len(A)):
          while(len(stack) != 0  and stack[len(stack)-1] >= A[idx]):
              stack.pop()
          if len(stack) != 0 :
              result[idx] = stack[len(stack)-1]
          stack.append(A[idx])
              
      return result

