# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float('inf')
        self.pre = -float('inf')
        def dfs(root):
            if not root:
                return 0
            dfs(root.left)
            # print(left, root.val)
            
            ans = root.val-self.pre
            self.pre = root.val
            self.minDiff = min(self.minDiff, ans)
            dfs(root.right)
            # print(ans)
            return ans
        dfs(root)
        return -1 if self.minDiff == float('inf') else self.minDiff
            
# semi solved..here main scene was that maintain pre ye islie because example 2 me jab 0 tha
# tb ek h node se min diff aa gya bt yahn 2 nodes k beech ka bola
# islie ye pre k maintain krke single node kabhi max de h na paega because 0-(-float(inf)) which
# is +float('inf') toh h jaega scene and then two nodes ka dekhnge scene 
