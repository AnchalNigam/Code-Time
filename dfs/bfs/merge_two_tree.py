# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(root1, root2):
            if root1 is None and root2 is None:
                return None
            ans = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
            ans.left = solve(root1 and root1.left, root2 and root2.left)
            ans.right =  solve(root1 and root1.right, root2 and root2.right)
            # print(self.ans.val)
            return ans
        return solve(root1, root2)

# was confused..i was trying to change root1 but we should have done using separate node
# because it asked ki naya tree banao toh naya banap..frst issue questn k solve krne me ye
# hua ki naya sochna tha tree....dusre chez ki make new node and attach krte jao 
        
        