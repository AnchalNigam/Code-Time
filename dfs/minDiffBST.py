# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float('inf')
        def inorder(node):
            if node.left:
                inorder(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            if node.right:
                inorder(node.right)
        inorder(root)
        return self.ans


# here main funda is adjacent nodes ka diff maintain krte chalo j min hga maintain kro
# other way is pehle inorder nikal lo then array me adjacent values me min dhundho , same recursion
# se achieve kia
# time complexity - o(n) as we are traversing every node
# space - o(1)