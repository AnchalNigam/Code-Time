# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = [False]
        def solve(root, target):
            if root:
                if ans[0]:
                    return True
                if (target-root.val) == 0:
                    if root.left is None and root.right is None:
                        ans[0] = True
                        return True
                solve(root.left, target-root.val)
                solve(root.right, target-root.val)
        solve(root, targetSum)
        return ans[0]

# see above we have break the recursion byusing outer variable and maintaining that

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(root, target):
            if root:
                if (target-root.val) == 0:
                    if root.left is None and root.right is None:
                        return True
                return solve(root.left, target-root.val) or solve(root.right, target-root.val)
            else:
                return False
        return solve(root, targetSum)

# this sol is not using any outer variable, just using return statement. ere return statement is
# playing role..when got the left ans then return it and use or then check for it and
# both ans or operator use...return we can use

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(root, target):
            if root is None:
                return False
            if root.left is None and root.right is None:
                return target == root.val            
           
            left = solve(root.left, target-root.val) 
            if(left):
                return True
            right = solve(root.right, target-root.val)
            return left or right
         
        return solve(root, targetSum)
       
    
        
# i like this because hre if we get root to leaf sum as true then why to go to right sibtree
# just break the recursion so for that either use frst approach or last one...in last one we are storing 
# ans using return and then checking if its true then why to compure rigt subtree
# maza aya...one more thing here target < 0 ni lia because tree can have negative values as well
       
            