# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.freqMapper = {}
        def isPseduoPalindrome(n):
            even = 0
            odd = 0
          
            for key, value in self.freqMapper.items():
                if value % 2 == 0:
                    even += 1
                else:
                    odd += 1
            if n%2 == 0 and odd > 0:
                return False
            elif n%2 != 0 and odd > 1:
                return False
            return True
        self.result = 0      
        def helper(root, c):
            if not root:
                return 
            if not root.left and not root.right:
                # print(root.val, 'check', self.freqMapper)
                if root.val not in self.freqMapper:                
                    self.freqMapper[root.val] = 1
                else:
                    self.freqMapper[root.val] += 1
                isPalin = isPseduoPalindrome(c+1)
                if isPalin:
                    self.result += 1
                return
            # print(self.freqMapper, root.val)
            if root.val not in self.freqMapper:                
                self.freqMapper[root.val] = 1
            else:
                self.freqMapper[root.val] += 1
            helper(root.left, c+1)
            if root.left:
                if self.freqMapper[root.left.val]-1 == 0:                
                    del self.freqMapper[root.left.val]
                else:
                    self.freqMapper[root.left.val] -= 1
            helper(root.right,c+1)
            if root.right:
                if self.freqMapper[root.right.val]-1 == 0:                
                    del self.freqMapper[root.right.val]
                else:
                    self.freqMapper[root.right.val] -= 1
        helper(root, 0)
        return self.result
# i did it by own...wowwww...
# general logic freq maintain rkho and end me palin check kro
# scene is 
# time complexity - o(nk) as n nodes we are traversing, k is distict element in dic to check palin
# spce -o(k+h) - h is height of tree[recursion j use kr rha hai] and k is dic me distinct
# elem
# space is o(h+k) which in worst case is o(n+k) in case of linear linkedlist wala scene