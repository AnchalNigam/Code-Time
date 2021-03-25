stack = []
A = [27, 11, 4, 24, 32, 32, 1]
result = [-1 for idx in range(len(A))]
if len(A) == 0:
    print(result)
stack.append(A[0])
for idx in range(1, len(A)):
    while(len(stack) != 0  and stack[len(stack)-1] >= A[idx]):
        stack.pop()
    if len(stack) != 0 :
        result[idx] = stack[len(stack)-1]
    stack.append(A[idx])
        
print(result)