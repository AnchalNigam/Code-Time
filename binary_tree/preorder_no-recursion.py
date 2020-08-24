def preorderTraversal(self, A):
  stack = []
  preOrderNodes = []
  while True:
      if A != None:
          preOrderNodes.append(A.val)
          stack.append(A)
          A = A.left
      elif len(stack) != 0:
          poppedElem = stack.pop()
          A = poppedElem.right
      else:
          break
  return preOrderNodes