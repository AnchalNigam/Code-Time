from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(1, m):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    print(i, j)
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        # print(triangle)
        minVal = float('inf')
        for i in range(m):
            minVal = min(minVal, triangle[m-1][i])
        return minVal
        
# here basic idea is to store all previous paths...if i am at level [2][1] so [2][1] tak
# ane k ways me j min path h wo store kro so [2][1] tak ane k [1][1] and [1][0] hai way
# so whoever is min store it.....in this way it will be solved
# time complexity - o(n2), no space as changing the same matrix 