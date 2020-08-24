def inorderTraversal(self, A):
  stack = []
  nodesVal = []
  while True:
      if A != None:
          stack.append(A)
          A = A.left
      elif len(stack) != 0:
          poppedElem = stack.pop()
          nodesVal.append(poppedElem.val)
          A = poppedElem.right
      else:
          break
  return nodesVal