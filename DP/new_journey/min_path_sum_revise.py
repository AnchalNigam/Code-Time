class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i != 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                elif i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        # print(grid)
        return grid[m-1][n-1]
            
# solved it...same store the result of previous up cell and left cell and whoever is min take that 
# and add it in curr cell so this will be min cost to reach that cell...so memo krke we found
# ans..time complexity - o(n2)..space no