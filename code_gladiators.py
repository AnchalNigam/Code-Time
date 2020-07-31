arr = [3, 6, 7, 5, 3, 5, 6, 2, 9, 1 ]
arr2 = [2, 7, 0, 9, 3, 6, 0, 6, 2, 6 ]
# def bin_search(arr, n, x): 
#   l = 0
#   h = n - 1
#   flag = False
#   while(l <= h): 
#       mid = int((l + h) / 2) 
#       # if 'x' is greater than or equal to arr[mid],  
#       # then search in arr[mid + 1...h] 
#       if(arr[mid] > x): 
#         flag = True
#         h = mid - 1; 
#       else: 
#       # else search in arr[l...mid-1] 
#         l = mid + 1
#   # required index 
#   if flag:
#     return h
#   return -1
# def countElements(arr1, arr2, m, n): 
#   # sort the 2nd array 
#   arr2.sort() 
#   count = 0
    
#   # for each element in first array 
#   for i in range(m): 
#       # last index of largest element  
#       # smaller than or equal to x 
#       index = bin_search(arr2, len(arr2), arr1[i]) 
#       if index!=-1:
#         count += 1
      
#       # required count for the element arr1[i] 
#         arr2.pop(index) 
#   print(count)
# countElements(arr2,arr,len(arr), len(arr2))
# count = 0
# for value in arr2:
#     maxVal = float('inf')
#     flag = False
#     index = 0
#     while index < len(arr):
#         print(arr[index], index, value, '++')
#         if arr[index] > value and arr[index] < maxVal:
#             maxVal = arr[index]
#             flag = True
#         index += 1
#     print(maxVal, flag)
#     if flag:
#         count += 1
#         findIndex = arr.index(maxVal)
#         arr.pop(findIndex)
# print(count)
import heapq
heapq.heapify(arr)
heapq.heapify(arr2)
print(arr, arr2)

for t in range(T):
        n = int(input())
        ourPower = list(map(int, input().split()))
        opponentPower = list(map(int, input().split()))
        count = 0
        ourPower.sort()
        opponentPower.sort()
        while len(ourPower) > 0:
            if ourPower[0] > opponentPower[0]:
                count += 1
                ourPower.pop(0)
                opponentPower.pop(0)
            else:
                ourPower.pop(0)
        print(count)