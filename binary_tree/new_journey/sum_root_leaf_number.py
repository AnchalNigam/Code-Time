# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.ans
    def dfs(self, root, summ):       
        if root is None:
            return 0
        if root.left is None and root.right is None:
            self.ans += (summ*10) + root.val
            return
        self.dfs(root.left, summ*10 + root.val)
        self.dfs(root.right, summ*10 + root.val)

# Time Complexity : O(N), where N is the number of nodes in the tree. We are doing a standard DFS traversal which takes O(N) time
# Space Complexity : O(H), where H is the maximum depth of tree. This space is required for implicit recursive stack space. In the worst case, the tree maybe skewed and H = N in which case space required is equal to O(N).