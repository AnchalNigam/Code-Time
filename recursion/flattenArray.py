def flattenArray(arr, res):
  for idx in range(len(arr)):
    if isinstance(arr[idx], list):
      flattenArray(arr[idx], res)
    else:
      res.append(arr[idx])
  return res

print(flattenArray([[1], [2, 3], [4], [3, [2, 4]]], []))


