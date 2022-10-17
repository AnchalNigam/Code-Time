from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.res = 0
        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return 
            if grid[i][j] == '*' or grid[i][j] == 0:
                return
            grid[i][j] = '*'
            self.res += 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    maxArea = max(maxArea, self.res)
                 
                    self.res = 0
        return maxArea