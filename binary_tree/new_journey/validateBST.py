# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root, minVal, maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False
            left = solve(root.left, minVal, root.val)
            if not left:
                return False
            right =  solve(root.right, root.val, maxVal)
            return left and right
        return solve(root, float('-inf'), float('inf'))
       
        
        
# semi solved,,,,so here main scene ki at each level, you need to maintain min and max and acc
# check values 
        