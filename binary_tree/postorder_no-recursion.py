def postorderTraversal(self, A):
  root = A
  stack = []
  postOrderTraversal = []
  while True:
      if root is not None:
          stack.append(root)
          root = root.left
      elif(stack):
          node = stack[len(stack)-1]
          if(node.right):
              current = node.right
              node.right = None
          else:
              postOrderTraversal.append(stack.pop().val)
      else:
          break
  return postOrderTraversal
                