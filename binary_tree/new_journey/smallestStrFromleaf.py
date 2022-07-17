# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result = ""
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        def solve(root, res):
            if not root:
                return
            if not root.left and not root.right:
                res = self.alphabet[root.val] + res
                a = len(self.result)
                b = len(res)
                if self.result == "":
                    self.result = res
                else:
                    mini = min(a, b)
                    if self.result[:mini+1] > res[:mini+1]:
                        self.result = res
                return
            
            solve(root.left, self.alphabet[root.val]+res)
            solve(root.right, self.alphabet[root.val]+res)
        solve(root, "")
        return self.result

# did this by own..applied logic of normal paths finding....hee main challenge was that 
# u need to reversly check so maine res me ulta add kia and second har cases bana ke
# i did this   if self.result[:mini+1] > res[:mini+1]:
                        # self.result = res
# so maine isse ye sekha...check constraints thoroughly + har cases sochne k koshish kro