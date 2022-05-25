from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):      
            left = 0
            right = n-1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1

# unfortunately, i was not able to solve it but i learnt how to approach these rotatn wala
# questns, in this questns u cant reach directly to answers..i was approaching directly
# 90 deg rotate directly kr lo but here u have to frstly make matrix to come in one stage
# then actual answer pe lao...mainly transpose kra then swap kr dia frst and last column k
# swcond and second last col k..
# for 180, frst col swap frst and last , second and second last and then again swap rows in similar fashon
# for 270, swap row instead of col
# Code will be similar for all the approaches, applying transpose and swapping(using 2 Pointers) in different order, 
# gives us different results, This is how we can do it inplace.
# so swapping rows and columns and transpose will give us result
