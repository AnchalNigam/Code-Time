from itertools import permutations
T = input()
# def countTriplets(arr):
#   combinationArr = list(combinations(arr, 3))
#   count = 0
#   print(combinationArr)
#   for indx in range(len(combinationArr)):
#     if (combinationArr[indx][0] + combinationArr[indx][1] == combinationArr[indx][2]) or (combinationArr[indx][0] + combinationArr[indx][2] == combinationArr[indx][1]) or (combinationArr[indx][1] + combinationArr[indx][2] == combinationArr[indx][0]):
#       count += 1
#   if count == 0:
#     return -1
#   else:
#     return count
# for i in range(int(T)):
#   sizeArr = input()
#   arr = input().split()
#   print(arr)
#   floatArr = list(map(float, arr))
#   arr = list(map(int, floatArr))
#   print(countTriplets(arr))


# T = input()
# def countTriplets(arr):
#   count = 0
#   for indx in range(len(arr)):
#     for indx2 in range(indx+1, len(arr)):
#       if (arr[indx] + arr[indx2]) in arr:
#         count += 1
#   return count
