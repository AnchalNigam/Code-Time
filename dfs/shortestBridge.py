from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0 :
                return
            if grid[i][j] == 0 or (i, j) in visit:
                return
            visit.add((i, j))
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i-1, j)
            dfs(i, j+1)
        
        def bfs():
            res = 0
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            queue = deque(visit)
            # print(queue)
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        currR, currC = r+dr, c+dc
                        if currR >= m or currC >= n or currR < 0 or currC < 0 or (currR, currC) in visit:
                            continue
                        if grid[currR][currC]:
                            return res
                        visit.add((currR, currC))
                        queue.append((currR, currC))
                # print(res)
                res += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    return bfs()

  # i was not able to solve but ya i leant here that frst find what is our first island
  # put it in queue and then use bfs on each cell to reach destination cell and maintaining
  # res answer..here one layer like jumping to all next cell then push it into queue then
  # again ..another row of cells take and go to next cell(layer layer bfs h rha hai) till destination
  # ye logic h 