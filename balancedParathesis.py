def solve(A):
  stack = []
  stack.append(A[0])
  for idx in range(1, len(A)):
    if A[idx] == "(":
      stack.append(A[idx])
    elif len(stack) != 0:
      if stack.pop() != "(":
        return 0
    else:
      return 0
  if len(stack) != 0:
    return 0
  return 1


  


print(solve("(()())"))