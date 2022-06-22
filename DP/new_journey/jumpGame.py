import logging
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n-1
        dp = [False]*n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            if (last-i) <= nums[i]:
                dp[i] = True
                last = i
        return dp[0]

# solved it by own...yoo ..complexity is o(n)
# main funda is we will check from last..if its possible to react last index then obvio its possible
# frst last would be last elem of arr then wll go to n-2 if its false then last would still be
# last elem of arr..now if n=3 pe true aa gya then last would be now 3 and now weill check ki n=3
# pe possible h ana from any index or not, if yes meansing we can also reach to last..ye h hai logic