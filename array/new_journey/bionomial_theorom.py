def bionomial(n, r):
  if n < r:
    return 0
  arr = [[1], [1,1]]
 
  for i in range(2, n+1):
    sub = [1]
    for j in range(1, r):
      sub.append(arr[i-1][j]+arr[i-1][j-1])
    arr.append(sub)
  print(arr)
  return arr

print(bionomial(4, 3))

