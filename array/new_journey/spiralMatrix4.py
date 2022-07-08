# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        resArr = [[-1 for j in range(n)] for i in range(m)]
        tmp = head
        row = 0
        col = 0
        d = "R"
        while tmp:
            if d == "R": 
                if col < n and resArr[row][col] == -1:
                    resArr[row][col] = tmp.val
                    col += 1   
                    tmp = tmp.next
                else:
                    col -= 1
                    row += 1
                    # print(tmp.val, row, col)
                    d = "D"
            elif d == "D":
                if row < m and resArr[row][col] == -1:
                    resArr[row][col] = tmp.val
                    # print(resArr, 'check')
                    tmp = tmp.next
                    row += 1
                else:
                    col -= 1
                    row -= 1
                    # print(tmp.val, 'val')
                    d = "L"
            elif d == "L":
                if col >= 0 and resArr[row][col] == -1:
                    resArr[row][col] = tmp.val
                    # print(resArr, 'checkL')
                    col -= 1
                
                    tmp = tmp.next
                else:
                    col += 1
                    row -= 1
                    d = "U"
            elif d == "U":
                # print(row, col,'roww', tmp.val)
                if row >= 0 and resArr[row][col] == -1:
                    resArr[row][col] = tmp.val
                    # print(resArr, 'checkU')
                    row -= 1
                    tmp = tmp.next
                else:
                    col += 1
                    row += 1
                    d = "R"
          
        return resArr
            

# i did it by own..i used spiral matrix logic with little tweaking to implement it
                
        