from typing import List


class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    n = len(matrix)
    m = len(matrix[0])
    res = []
    d = "R"
    row = 0
    col = 0
    
    while len(res) < n*m:
        # print(row, col, 'check', res)
        if d == "R":
            if col < m and matrix[row][col] != -101:
                res.append(matrix[row][col])
                matrix[row][col] = -101
                col += 1  
            else:
                d = "D"
                row += 1
                # print(row, 'inside')
                col -= 1
        elif d == "D":
            if row < n and matrix[row][col] != -101:
                res.append(matrix[row][col])
                matrix[row][col] = -101
                row += 1
            else:
                d = "L"
                row -= 1
                col -= 1
        elif d == "L":
            if col > -1 and matrix[row][col] != -101:
                res.append(matrix[row][col])
                matrix[row][col] = -101
                col -= 1
            else:
                d = "U"
                row -= 1
                col += 1
        elif d == "U":
            if row > -1 and matrix[row][col] != -101:
                res.append(matrix[row][col])
                matrix[row][col] = -101
                row -= 1
            else:
                d = "R"
                row += 1
                col += 1
        
    return res   
            
        
            
        
# i solved it ...general approach whatever ques is saying simple use k lekr solve kia
# if already traversed that array then traversal stop kia so basic flow...o(n*m) as
# i am travesing all elements of matrix
            
        
    