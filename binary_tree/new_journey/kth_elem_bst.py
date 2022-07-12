# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.c = 0
        self.k = k
        self.res = None
        self.solve(root)
        return self.res
    def solve(self, root):
        # print(self.c, root and root.val)
        
        if not root:
            return 
        if self.c > self.k:
            return
        
        self.solve(root.left)
        self.c += 1
        if self.c == self.k:
            # print(root.val, 'check')
            self.res = root.val
            return
        self.solve(root.right)
   
# i did it using inorder traversal(leetcode check) but tried diff method as well which is above
# what i learned is if you want to have values in each recursion picture then use self.s 
# variable which is in other functn ...check whole gyan on this in notes section...
# incredible way told how variable access in nested functions and all..
# here as class is used so to get mutated value maintain rhe we can make c as instance variable
# as self.c and use kr skte hai..dusra way  nonlocale wala bhi hai see - nonlocale,c=[0], self.c
# three ways se tm handle kr skte h values [variable access ways in nested functn]

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.c = 0
        # self.k = k
        # self.res = None
        # self.solve(root)
        # return self.res
        c = 0
        res = 0
        def solve(root):
            nonlocal c
            nonlocal res
            # print(self.c, root and root.val)

            if not root:
                return 
            if c > k:
                return

            solve(root.left)
            c += 1
            if c == k:
                # print(root.val, 'check')
                res = root.val
                return
            solve(root.right)
        solve(root)
        return res
   
