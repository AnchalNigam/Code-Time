from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        result = [[0 for j in range(m)] for i in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]
        return result

# i did this mine....main funda whi swappping ka lagaya
# time complexity as its not square matrix..agr squae hta then we could have done inplace swapping
# as its not square one toh have to take new matrix so time complexity toh m *n hga
# and space bhi same o(m*n)..for sqauare space can be avoided by dong inplace - o(1)