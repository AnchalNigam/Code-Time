 def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        queue = [root]
       
        while len(queue) != 0:
            size = len(queue)
            for idx in range(size):
                popElem = queue.pop(0)
                if idx == 0:
                    result.append(popElem.val)
                if popElem.right:
                    queue.append(popElem.right)
                if popElem.left:
                    queue.append(popElem.left)
                    
        return result
                