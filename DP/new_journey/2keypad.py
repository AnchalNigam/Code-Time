class Solution:
    def minSteps(self, n: int) -> int:
        def highestPrimeFactor(n):
            for i in range(n//2, 1, -1):
                if n%i == 0:
                    return i
            return 1
        if n == 1:
            return 0
        dp = [0 for i in range(n+1)]
        dp[1] = 0
        dp[2] = 2
        for i in range(3, n+1):
            prime = highestPrimeFactor(i)
            dp[i] = dp[prime] + i//prime
        return dp[n]
            
#         main funda here is i was trying to figure out answer using previous computatn value
# i found patten whatever highest divisible candidate [before n//2], that value + whatever left prime//n this would be ans of current