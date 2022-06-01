from heapq import *
def find_k_largest_numbers(nums, k):
  result = []
  # TODO: Write your code here
  
  for num in nums:
    if len(result) < k:
      heappush(result, num)
    else:
      if num > result[0]:
        heappop(result)
        heappush(result, num)

  return result

# Time complexity 
# As discussed above, the time complexity of this algorithm is O(K*logK+(N-K)*logK), which is asymptotically equal to O(N*logK)
# Space complexity 
# The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.
# '''