
# M = [-1 for idx in range(9)]
# M[0] = 1
# M[1] = 1
# def fib(n):
#   if n == 0 or n == 1:
#     return 1
#   if M[n-1] == -1:
#     M[n-1] = fib(n-1)
#   if M[n-2] == -1:
#     M[n-2] = fib(n-2)
#   print(M)
#   return M[n-1] + M[n-2]

# print(fib(9-1))
#  if A == 0  or A == 1:
#     return 1
A = 4
M = [-1 for idx in range(A)]
M[0] = 1
M[1] = 1
def stairs(n):
  if n == 0 or n == 1:
    return 1
  if M[n-1] == -1:
    M[n-1] = stairs(n-1)
  if M[n-2] == -1:
    M[n-2] = stairs(n-2)
  return M[n-1] + M[n-2]

print(stairs(A))
