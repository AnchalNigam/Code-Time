# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaf = []
        self.res = False
        def helper(root, first):
            if self.res:
                return
            if not root:
                return
            if not root.left and not root.right:
                if first:                    
                    self.leaf.append(root.val)
                elif len(self.leaf) == 0:
                    self.res = True
                else:
                    if self.leaf[0] != root.val:
                        self.res = True
                    elif self.leaf[0] == root.val:
                        del self.leaf[0]
                return
            helper(root.left, first)
            helper(root.right, first)
        helper(root1, True)
        # print(self.leaf)
        helper(root2, False)
                
        return False if len(self.leaf) > 0 else not self.res
            
            
        
# did by own....general logic ek bare traverse kr lo then second one k sath 
# dekh lo
# time complexit - o(n+m) as n nodes 1 tree k traverse kia and m nodes 2nd 
# tree toh o(n+m)
# space - as array use kia toh no of leaf nodes in 1tree
# and aucilizary space (o(h1+h2+no of leaf nodes in 1tree))