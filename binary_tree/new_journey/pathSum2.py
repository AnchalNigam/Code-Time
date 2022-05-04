# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int):
        result = []
        def solve(root, target, res):
            if root is None:
                return 
            if root.left is None and root.right is None:
                if (target-root.val) == 0:
                    result.append(res + [root.val])
                return
            res.append(root.val)
            solve(root.left, target-root.val, res)
            solve(root.right, target-root.val, res)
            res.pop()
            
        solve(root, targetSum, [])
        return result
                
# here i used backtracking knowledge and dry run before running actual code and make sure whenever
# u write any code, dry run it, no hurry