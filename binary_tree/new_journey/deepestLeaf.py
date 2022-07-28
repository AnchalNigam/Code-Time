# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append([root])
        while queue:
            poppedLevel = queue.pop()
            levelArr = []
            levelNodes = []
            while poppedLevel:
                poppedNode = poppedLevel.pop()
                levelArr.append(poppedNode.val)
               
                if poppedNode.left:
                    levelNodes.append(poppedNode.left)
                if poppedNode.right:
                    levelNodes.append(poppedNode.right)
            if levelNodes:
                queue.append(levelNodes)
        return sum(levelArr)

# did by own..woooooww...
# level order traversal kia and yye logic lagaya j bhi last hga whi apna levelar me hga
# so done ....time complexity - o(n) as every node is traversed once
# space -  as max nodes kite hge ek level pe wo hga so say max node hai ek level
# pe w so o(w) + as we are using levelarr so that will use max width worst case me
# o(w) again + level nodes which in directly max node h hga so o(3w)