arr = [2,3,3,2,5]
n = len(arr)
for j in range(n):
  arr[j] = arr[j] - 1
 
for idx in range(n):
  arr[(arr[idx]%n)] += n

for idx in range(n):
  print(arr[idx]//n)


# o(n) , o(1) space above complexity