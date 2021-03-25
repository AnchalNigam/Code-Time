 def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
      
       def checkSum(root, summation):
            # print(summation, 'll')
        if root is None:
            return 0
        elif root.left is None and root.right is None and summation == S:
            # print(summation, targetSum, 'test')
            return True
        # elif root is None or (root.left is None and root.right is None):
        #     return 0
        
        if root.left:
            leftNode = checkSum(root.left, summation+root.left.data)
        else:
            leftNode = 0
        if root.right:
            rightNode = checkSum(root.right, summation+root.right.data)
        else:
            rightNode = 0
            
        return leftNode or rightNode
    if root is None:
        return False
    
    return checkSum(root, root.data)
        