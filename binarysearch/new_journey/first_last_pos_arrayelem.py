def searchRange(A, target):
  n = len(A)-1
  low = 0
  high = n
  flag = False
  while low <= high:
      mid = low + ((high-low)//2)
      if A[mid] == target:
          flag = True
          break
      elif A[mid] > target:
          high = mid-1
      else:
          low = mid+1
  if not flag:
      return [-1, -1]
  high2 = mid-1
  low2 = mid+1
  while low <= high2:
      mid = low + ((high2-low)//2)
      if A[mid] == target:
          high2 = mid-1
      else:
          low = mid+1
  while low2 <= high:
      mid = low2 + ((high-low2)//2)
      if A[mid] == target:
          low2 = mid+1
      else:
          high = mid-1
  return [low, high] 

# i solved it in o(logn). so basic funda what i used is first find out whether u have got that search 
# elem or not. if no then simply return [-1,-1] else after finding elem we hav to find its left
# most indices and right most. so what i did i again divided that search range in two parts
# on left part iff i found again mid as target then i will go left again and again until i
# found not target so left most indices we can find. similarly for right most indices, we 
# go right most (low2=mid+1) till we ae finding target elem else high = mid-1
# this is logic
      