def minimizeSum(arr):
  import heapq
  heapq.heapify(arr)
  summation = 0
  result = 0
  while len(arr) > 1:
      firstMin = heapq.heappop(arr)
      secondMin = heapq.heappop(arr)
      summation = firstMin+secondMin
      heapq.heappush(arr, summation )
      print(arr)
      result += summation
  return result

# one thing i have learned in heap if any question related to runtime array change and extracting 
# something and all use heap then see minimize the sum example