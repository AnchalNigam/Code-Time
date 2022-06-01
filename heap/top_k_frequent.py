from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        nums = []
        for num, freq in dic.items():
            heappush(nums, (-freq, num))
        result = []
        for i in range(k):
            result.append(heappop(nums)[1])
        return result
            
            
# here basic knowledge is ti use heap...
# time n + nlogn +k we can imporove it by makig heap of k elements only..toh n + nlogk + k h hta
# see below..space - Space complexity 
# The space complexity will be O(N). Even though we are storing only ‘K’ numbers in the heap. 
# For the frequency map, however, we need to store all the ‘N’ numbers.


from heapq import *


def find_k_frequent_numbers(nums, k):

  # find the frequency of each number
  numFrequencyMap = {}
  for num in nums:
    numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1

  minHeap = []

  # go through all numbers of the numFrequencyMap and push them in the minHeap, which will have
  # top k frequent numbers. If the heap size is more than k, we remove the smallest(top) number
  for num, frequency in numFrequencyMap.items():
    heappush(minHeap, (frequency, num))
    if len(minHeap) > k:
      heappop(minHeap)

  # create a list of top k numbers
  topNumbers = []
  while minHeap:
    topNumbers.append(heappop(minHeap)[1])

  return topNumbers