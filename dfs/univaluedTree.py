# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.ans = False
        def solve(root, res, value):
            if self.ans:
                return
            
            if not res:
                self.ans = True
                return
            if not root:
                return True
            # print(root.val, value, root.val == value, res)
          
          
            solve(root.left, root.val == value, root.val)
            solve(root.right, root.val == value, root.val)
            
            
        solve(root, True, root.val)
        return not self.ans

# solved, in this what i did, i passed the value in function(inspired by its bst ornot questn)
# from above passing value and if res is false meaning mismatch hua then main ans ko set kr do
# and fr koi recursion call k andar h na jane do upar se h if self.ans true toh return 
# here back track ka scene use kia end jab h gya then ans maintain kia and return aise h kra dia

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.ans = False
        def solve(root, value):
            if not root:
                return True
            if root.val != value:
                return False
            res1 = solve(root.left, root.val)
            res2 = False
            if res1:
                res2 = solve(root.right, root.val)
            return res1 and res2
            
        return solve(root, root.val)
# here explicictly res na lekr i have put falsy condition and then res1 and res2 maintain krke
# return kia