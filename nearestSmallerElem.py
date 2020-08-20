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

