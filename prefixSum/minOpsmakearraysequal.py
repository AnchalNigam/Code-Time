from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        from itertools import accumulate
        from bisect import bisect_left
        nums.sort()
        def findIdx(number):
            low = 0
            high = n
            while low <= high:
                mid = low + (high-low)//2
                # print(mid, low, high, nums)
                if nums[mid] == number:
                    return mid
                elif nums[mid] < number:
                    low = mid + 1
                else:
                    high = mid-1
            return low

       
        prefix = [0] + list(accumulate(nums))
        n = len(nums)-1
        res = []
        for q in queries:
            i = findIdx(q)
            j = bisect_left(nums, q)
            # print(j, i, prefix, n)
            # print(i)
        
            ans = (((i)*q - prefix[i])+((prefix[n+1]-prefix[i])-(n-i+1)*q))
            res.append(ans)
        return res


# after sorting num
# in this prob main logic is find index that is less than q [wo value j array k sb element k banana hai]
# prefix sum calculate kr lete hai
# now that index meaning whn tak k sare elements k inc krna h to q meaning ideally
# index i tak j sum hna chahye ar j hai use subtract kr lete hai
# similarly index k bad k elements k dec krna hga to q meaning j prefix[n] hga-prefix[i] kita 
# sum hai ar ideally hna chhaye minus that...is whole logic k implement kia gya h
# to handle edge cases better like if q is nt present in array then uska calc and i > n 
# and so on hmne prefix sum k n+1 k banaya