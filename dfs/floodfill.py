from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return
            
            if image[i][j] != x or image[i][j] == color:
                return
            image[i][j] = color
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i-1, j)
        x = image[sr][sc]
        # print(x)
        dfs(sr, sc)
        return image
        
# i solved it with same logic of max island ki agr wo viisted h then vist na kro and 
# if its equal to value that we dont want to tranverse then return else process
