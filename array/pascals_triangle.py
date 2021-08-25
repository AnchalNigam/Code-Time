class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        result = []
        if A == 0:
            return result
        result.append([1])
        for i in range(1, A):
            row = []
            row.append(1)
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
        return result
# for better understanding(if not understaing from here, look nick white video)