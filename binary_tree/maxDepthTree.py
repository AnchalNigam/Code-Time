def maxDepth(self, root: TreeNode) -> int:
  if root is None:
    return 0
  else:
    ldepth = self.maxDepth(root.left)
    rdepth = self.maxDepth(root.right)
    
    if(ldepth < rdepth):
      return rdepth + 1
    return ldepth + 1
