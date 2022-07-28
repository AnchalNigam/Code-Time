# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def solve(root):
            if not root:
                return True
            if not root.left and not root.right:
                if root.val == target:
                    return True
                return False
            
            left = solve(root.left)
            if left:
                root.left = None
            right = solve(root.right)
            if right:
                root.right = None
            return left and right and root.val == target
        ans = solve(root)
        if ans and root.val == target:
            return None
        return root
            
# did it by own...what i have done go at leaf..check leaf.value = target 
# then return true and make left child of upper node to none
# then if right one bhi aisa hga toh same ..then agr dono h true return kie
# upper node k and node itself has val = target then that must be deleted
# meaning return true so int his way solved 
# time complex- as all node traverse once so o(n)
# space - o(h) as recursion me left subtree pop krne k bad right uthate toh
# o(h) and skewed tree me o(n) [linkedlist scene]