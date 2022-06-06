class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summation = 0 
        n = len(stones)
        for i in range(len(stones)):
            summation += stones[i]
        hs = summation // 2
        dp = [[-1 for i in range(hs+1)] for j in range(n)]
        result = [float('inf')]
        def solve(n, target):
            if n >= len(stones):
                return target
            if dp[n][target] != -1:
                return dp[n][target]
            pick = float('inf')
            if stones[n] <= target:
                pick = solve(n+1, target-stones[n])
            nonPick = solve(n+1, target)
            dp[n][target] = min(pick, nonPick)
            return dp[n][target]
        solve(0, hs)
        return summation - (2*(hs-dp[0][hs]))

# this questn gets molded into knapsack..it is said that agr hm two partition me stones 
# divide kre and then try to get sum that is closer to sum/2 this means s1+s2 = sum
#  s2  = s1-(sum-s1) = sum-2s1 ab hme ye pta krna hai kya s1/2 some possible h given elems se
# ya fr uske close sum kya hai with those elems ..its kinda of knapsack where closer sum dhundhna hai
# thats why i tried finding ki if n=5 mns 5 elements and sum is 11 then its possible to make 
# 11 if yes suppose 10 tak bana skte hai toh target jita left hga like 1 left if we can
# make 10 sum so target left we have found and then actual sum ban kita paya i.e 10 
# can be figure out by subtracting with actual sum(hs) that we wanted to knwo that can be made or anything closer
# then above formular calculate
# time complexity - 
# Time Complexity: O(N*W). 
# where ‘N’ is the number of weight element and ‘W’ is capacity. As for every weight element we traverse through all weight capacities 1<=w<=W.
# Auxiliary Space: O(N*W). 