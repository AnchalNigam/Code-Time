 def isBalanced(self, root: TreeNode) -> bool:
  subTree = [True]
  def checkDepth(root):
      if root is None:
          return 0
      if subTree[0]:                
          ldepth = checkDepth(root.left)
          rdepth = checkDepth(root.right)
          if subTree[0]:                    
              if abs(ldepth-rdepth) > 1:
                  subTree[0] = False
              else:
                  subTree[0] = True
              if ldepth >= rdepth:
                  return ldepth + 1
              return rdepth + 1

  checkDepth(root)
  print(subTree)
  if not subTree[0]:
      return False
  return True
  