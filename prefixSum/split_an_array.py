from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0]*(n+1)
        count = 0
        for i in range(1,n+1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
        # print(prefixSum)
        for i in range(1, n):
            # print(prefixSum[n], prefixSum[i], n)
            if prefixSum[i] >= (prefixSum[n]-prefixSum[i]):
                count += 1
        return count
# did by own..yo man!
# complexity is o(n)
# maine prefix ka logic lagaya ki bhai har index pe jaunge and check krunge whn tak ka sum
# ar (dusre wale array k actual sum = dusre array k last tak sum -pehle wale array k sum) minus krke bada h toh bs count+=1