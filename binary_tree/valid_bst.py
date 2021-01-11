 def isValidBST(self, root: TreeNode) -> bool:
  nodesArr = []
  preOrder = []
  while True:
    if root:
      nodesArr.append(root)
      root = root.left
    elif(len(nodesArr) != 0):
      root = nodesArr.pop()
      preOrder.append(root.val)
      root = root.right                 
    else:
      break
  for idx in range(len(preOrder)-1):
    if preOrder[idx] >= preOrder[idx+1]:
      return False
  return True
          

# arr = [1,2,3,4,5]

# def binarySearch(arr, searchKey):
#   low = 0
#   high = len(arr)
#   while low <= high:
#     mid = low + ((high - low)//2)
#     if arr[mid] == searchKey:
#       return mid
#     if searchKey < arr[mid]:
#       high = mid - 1
#     else:
#       low = mid + 1
#   return mid

# print(binarySearch(arr,5))
# median arrya interviewbit
# def findMedianSortedArrays(A, B):
#   B = list(B)
#   A = list(A)
#   def binarySearch(arr, searchKey):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#       # print(searchKey)
#       mid = low + ((high - low)//2)
#       # print(mid, 'mid')
#       if arr[mid] == searchKey:
#         return mid
#       if searchKey < arr[mid]:
#         high = mid - 1
#       else:
#         low = mid + 1
#     return low
#   for elem in A:
#     mid =  binarySearch(B, elem)
#     B.insert(mid, elem)
#   if len(B)%2 == 0:
#     mid = len(B)//2
#     return (B[mid]+B[mid-1])/2
#   else:
#     return B[len(B)//2]
# print(findMedianSortedArrays([0,23], []))