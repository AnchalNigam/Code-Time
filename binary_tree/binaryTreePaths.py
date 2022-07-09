# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def getPaths(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            # print(root.val)
            self.result.append(res + str(root.val))    
        self.getPaths(root.left, res + str(root.val)+'->')
        self.getPaths(root.right, res+ str(root.val)+'->')
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.result = []
        self.getPaths(root, '')
        return self.result
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def backtrack(node, tmp):
            if not node:
                return
            if not node.left and not node.right:
                tmp.append(str(node.val))
                res.append("->".join(tmp[:]))
                return

            tmp.append(str(node.val))
            if node.left:
                backtrack(node.left, tmp)
                tmp.pop()
            if node.right:
                backtrack(node.right, tmp)
                tmp.pop()

        backtrack(root, [])
        return res
# done by me ...geenral dfs knowledge i applied...second version is of backtracking