# 1st way
arr = [1,2,3,4,5,6,7]
k = 3
# newArr = []
# for idx in range(k,0,-1):
#   newArr.append(arr[len(arr)-idx])

# for idx in range(len(arr)-k):
#   newArr.append(arr[idx])

# print(newArr)


# 2nd way
length = len(arr)
for idx in range(k):
  elem = arr[length-1]
  arr.pop(length-1)
  arr.insert(0, elem)
print(arr)
