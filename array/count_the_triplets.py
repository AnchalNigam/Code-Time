def countTriplet(arr, n):
		# code here
  count = 0
  arr.sort()
  for idx in range(n-1, 0, -1):
    k = idx-1
    j = 0
    while j < k:
      if (arr[j]+arr[k]) == arr[idx]:
        count += 1
        j += 1
        k += 1
      elif (arr[j]+arr[k]) < arr[idx]:
        j += 1
      else:
        k -= 1
  return count

arr = [3,6,8,11,12,14]
print(countTriplet(arr, len(arr)))