from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = 0
        n = len(nums)
        maxAvg = float('-inf')
        summ = 0
        while end < n:
            summ += nums[end]
            if (end-start) == k-1:
                maxAvg = max(maxAvg, summ/k)
                summ -= nums[start]
                start += 1
            end += 1
            
        return maxAvg