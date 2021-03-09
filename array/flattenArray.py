def getFlattenArray(arr):
  result = []
  def flattenArray(newArray):
    print(newArray, 'new')
    for elem in newArray:
      if isinstance(elem, list):
        flattenArray(elem)
      else:
        result.append(elem)
  flattenArray(arr)
  return result


print(getFlattenArray([1,[[2],3],4]))