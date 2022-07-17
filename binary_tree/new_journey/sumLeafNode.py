# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def helper(root):
            # print(root)
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
           
            left = helper(root.left)   
            # print(left, 'pp')
            right = helper(root.right)
            self.result += left
            return 0
        helper(root)
        return self.result
                
# i did this by thinking recursively..did by own/
# Time Complexity: O(N), where N is the number of nodes in the given binary tree. It is a standard DFS traversal technique where each node is visited once.
# Space Complexity : O(H), where H is the height of given binary tree. It is required for implicit recursive stack space. H = logN in case of a complete binary tree and H=N in case of a skewed tree.

