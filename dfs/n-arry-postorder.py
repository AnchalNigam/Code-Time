
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def solve(root):
            if root is None:
                return None
            if root.children:
                for child in root.children:
                    solve(child)
            ans.append(root.val)
            
          
        solve(root)
        return ans
# solved by own..main logic lagaya maine ki agr children h toh sbko traverse krke fr root k val
# store krao and so on...time complexity whi 0(n)