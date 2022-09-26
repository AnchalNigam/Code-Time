from typing import List
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        badPairs = 0
        ans = 0
        dic = defaultdict(int)
        n = len(nums)
        total_pairs = n * (n-1) / 2
        for i in range(n):
            x = nums[i]-i
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
        for key, value in dic.items():
            if value > 1:
                ans += value*(value-1)/2
        # print(ans)
        return int(total_pairs-ans)
# very interestng sol, i was not ablr to solve in optimized way..see general way is easy
# two loops concept, n2 complexity
# here main thing is they tried to keep nums[i]-i value in hashmap...if there is already exist
# ( j - A[j] ) != ( i - A[i] ) this eq is actually making this hasmap concept comes in market
# if there is already that value in hashmap means these two can make good pairs..so once we find
# such good pairs then see this https://leetcode.com/problems/count-number-of-bad-pairs/discuss/2426058/Java-or-Thought-process-Explained
# 
# n(n+1)/2 ka answer
# Lets say array is [1,2,3,4].
# For 1 , it will make pair with all previous elements i.e 0 pairs.
# For 2 , it will make pair with all previous elements i.e [1] which 1 pair.
# For 3 , it will make pair with all previous elements i.e [1,2] which is 2 pairs.
# For 4 , it will make pair with all previous elements i.e [1,2,3] which is 3 pairs.

# Now the total count of pair is = 0 + 1 + 2 + 3 which is sum of whole numbers i.e n * (n-1)/2 .

# We simply count the valid pairs from above equation and subtract it from total pairs in array i.e n* (n-1)/2.

# Invalid= n*(n-1)/2 - valid

