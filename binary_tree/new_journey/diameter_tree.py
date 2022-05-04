# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx = [0]
        def dfs(root):
            if root is None: 
                return 0
            lh = solve(root.left)
            rh = solve(root.right)
            maxx[0] = max(maxx[0], lh+rh)
            dfs(root.left)
            dfs(root.right)
        def solve(root):
            if root is None:
                return 0
            lh = solve(root.left)
            rh = solve(root.right)
            return 1 + max(lh, rh)
        dfs(root)
        return maxx[0]

# here main thought is at every node, we are calcutn left and right subtree and then adding both
# to give final answer and doing it for every node. o(n2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxx = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxx
    def dfs(self, root):
        if root is None:
            return 0
        lh = self.dfs(root.left)
        rh = self.dfs(root.right)
        self.maxx = max(self.maxx, lh+rh)
        return max(lh, rh)+1
     
# in this look i have made two public functns to make more code readable...anyways apart from readability
# look at that beaut of this soltn above soltn gets merged...here we are calcuting depth of particular
# node and then adding also at the same time to maintain maxx
      

      
