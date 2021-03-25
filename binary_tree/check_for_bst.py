 def isBST(self, root):
        #code here
        minVal = float('-inf')
        maxVal = float('inf')
        def checkBSTorNot(root, minVal, maxVal):
            if root is None:
                return True
            # print(root.data, minVal, maxVal)
            if root.data > minVal and root.data < maxVal:
                leftNode = checkBSTorNot(root.left, minVal, root.data)
                rightNode = checkBSTorNot(root.right, root.data, maxVal)
            else:
                return False
            # print(leftNode, rightNode, 'test')
            return leftNode and rightNode
        return checkBSTorNot(root, minVal, maxVal)
                
            