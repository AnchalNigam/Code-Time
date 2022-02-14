# def power2(n):
#   if n == 1:
#     return True
#   def solve(op):
#     if(op == n):
#       return True
#     if(op > n):
#       return False
#     return solve(op*2)
#   return solve(1)

def power2(n):
  if n <= 0:
    return False
  if(n == 1):
    return True
  return n%2 == 0 and power2(n//2)

print(power2(34))