class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if (A == 0):
            return [1]
        row = []
        row.append(1)
        prev = 1
        for i in range(A,1,-1):
            elem = prev*i//((A-i)+1)
            prev = elem
            row.append(elem)
        row.append(1)
        return row

# its basically looking from prev*n/1, prev*(n-1)/2 .....iske basis pe we are finding elem
