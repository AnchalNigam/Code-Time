def product(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return arr[0]
  return arr[len(arr)-1] * product(arr[:len(arr)-1])

print(product([1,2,3,4])) 