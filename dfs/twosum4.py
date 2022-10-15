# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.ans = False
        self.dic = {}
        def two_sum(root):
            if not root:
                return False
            if (k-root.val) in self.dic:                
                return True
            self.dic[root.val] =  1
            left = two_sum(root.left)
            right = False
            if not left:
                right = two_sum(root.right)
            return left or right
        return two_sum(root)
            
# in this i applied knowledge of two sum and uses same hashamp concept ....so use hashmap along with
# tree questn...also here if you find sum then return ans and to break recursion 
# just use same concept ki left me ans mila agr toh right me kyn jana and agr na
# mile ans toh right me jao and return left or right scene 