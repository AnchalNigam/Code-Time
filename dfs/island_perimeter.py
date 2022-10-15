from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.res = 0
        def dfs(i, j):
            # print(i, j)
            if i < 0 or j < 0 or i >= m or j >= n:
                self.res += 1
                return
            if grid[i][j] == 0:
                self.res += 1
                return
            if grid[i][j] == '*':
                return
          
            grid[i][j] = "*"
            dfs(i+1, j)
          
            # print(i, j, ';;;')
            dfs(i-1, j)
            # self.res += 1
            dfs(i, j+1)
            # self.res += 1
            dfs(i, j-1)
            # self.res += 1
            # grid[i][j] = curr
            # self.res += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    
        return self.res

# simple tha but still was not able to do because thought process n tha..
# isme simple scene ye h when u want to count perimeter , whe there is 0 and 
# 
# out of boundary so add 1 there and when there is 1 no entertainment…recursion 
# goes and goes into deep till the return statement not found then uske pehle wala
#  cell pick krega mns (3,1) [visualize 1st wala eg of this prob]...start (0,1) 
# -> (1,1)->(2,1)->(3,1)->(4,1) , 4,1 return kr dega now again it comes back to (3,1) 
# then (3,2) thne again back..(2,1) as its traversed so again back -> (3,0) , (3,1) which 
# is traversed so again back to (3,0) now go to (2,0) again return as its 0 (water) now 
# again back to (3,0) now go to (3,-1) again back-> now ab (2,1) ka dekhnge and then usko 
# krke fr (1,1) so is tarah se backtrack hta
