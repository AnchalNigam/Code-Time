# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum: int):
        result = []
        def solve(root, res, stack, target, r):
            if not root:
                return []
            if not root.left and not root.right and target == root.val:
                result.append(res[:]+[root.val])
                return
            stack.append(root)
            res.append(root.val)
            solve(root.left, res, stack, target-root.val, r)                   
            solve(root.right, res, stack, target-root.val, r)
            res.pop()
            root = stack.pop()
        if not root:
            return result
        solve(root, [], [], targetSum, False)
        return result
                
                