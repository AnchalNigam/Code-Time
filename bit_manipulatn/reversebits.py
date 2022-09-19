def reverse(A):
        #bit manipulation
  ans = 0
  
  for i in range(32):
      ans = (ans << 1) | (A&1)
      A = A >> 1
  return ans
print(reverse(12))