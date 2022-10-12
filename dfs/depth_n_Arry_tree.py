# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ans = 0
        def solve(root):
            if root is None:
                return 0
            depth = 0
            if root.children:
                for child in root.children:
                    depth = max(depth, solve(child))
                    
          
            return depth+1
        
        return solve(root)
# here quiet tickey, we are going to children and each children max depth kya h wo dekh rhe h
# ab jaise last me jaega depth+1 return hga max(0, returned value) aise kr kre depth h rha hai
# 0 yhn as such bs aise h rkha h to check its 
   
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        queue = [(root,1)]
        for (node, level) in queue:
            depth = level
            for child in node.children:
                queue.append((child, depth+1))
        return depth
# BFS TRAversal quite easy, traverse queue and node childdren and each children depth
# would increase by 1 so before appendinh to queue uske depth calc kr le rhe h and last
# jo bhi hga whi depth h toh scene aisa h
