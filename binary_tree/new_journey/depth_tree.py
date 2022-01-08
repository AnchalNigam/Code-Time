def maxDepth(root):
  if root is None:
    return 0
  lh = maxDepth(root.left)
  rh = maxDepth(root.right)
  return max(lh, rh) + 1

  