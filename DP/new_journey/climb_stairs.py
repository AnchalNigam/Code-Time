class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for idx in range(n)]
        def pairParty(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if dp[n-1] == -1:
                dp[n-1] = pairParty(n-1)
            if dp[n-2] == -1:
                dp[n-2] = pairParty(n-2)
            return dp[n-1] + dp[n-2]
        return pairParty(n)

# basic logic here is think about small inpit if n = 1 or n=2 mns these are the ways 1, 2 resp
# if new step is adding like 3 then 3rd one can be used as 1 step and if we remove last one 
# and account from last two, it means at a time 2 step wala case then mns adding of n-1 and n-2 
# would help. eventually fibonicci application