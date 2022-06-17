T = int(input())
result = []
def divisibleByI(n):
  result = [0] * n
  c1 = n
  c2 = 1
  c = 0
  for i in range(n-1, 0, -2):
    result[i] = c1
    result[i-1] = c2
    c1 -= 1
    c2 += 1
  if i == 2:
    result[i-1] = c1-1
    result[i-2] = c2
    
  return   ' '.join(map(str,result))
for t in range(T):
  n = int(input())
  result.append(divisibleByI(n))

for res in result:
  print(res)
