# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(root):
            if root is None:
                return None
            root.left, root.right = root.right, root.left
            solve(root.left)
            solve(root.right)
        solve(root)
        return root
# solved by own...logic is think of smaller entity and then revert left with reight and 
# then goto left and do...left left me jake revert na kia pehle revert kia fr left left me gye
