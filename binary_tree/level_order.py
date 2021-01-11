class Node:
  def __init__(self, data):
    self.left = None
    self.val = data
    self.right = None


def BFSTraversal(root):
  if root is None:
    return
  else:
    stack = []
    stack.append([root])
    stack2 = []
    stack2.append([root.val])
    while len(stack) > 0:
      poppedArr = stack.pop(0)
      levelArr = []
      while len(poppedArr) > 0:
        poppedLevelElem = poppedArr.pop(0)
        if poppedLevelElem.left is not None:
          levelArr.append(poppedLevelElem.left)
        if poppedLevelElem.right is not None:
          levelArr.append(poppedLevelElem.right)
      if len(levelArr) > 0:
        pushLevelArr = []
        for i in levelArr:
          pushLevelArr.append(i.val)
        stack2.append(pushLevelArr)
        stack.append(levelArr)
    return stack2

def BFSTraversal2(root):
  if root is None:
    return
  else:
    stack = []
    stack.append([root])
    stack2 = []
    stack2.append([root.val])
    while len(stack) > 0:
      poppedArr = stack.pop(0)
      levelArr = []
      while len(poppedArr) > 0:
        poppedLevelElem = poppedArr.pop(0)
        if poppedLevelElem and poppedLevelElem.left is not None:
          levelArr.append(poppedLevelElem.left)
        elif poppedLevelElem and poppedLevelElem.left is None:
          levelArr.append(None)
        if poppedLevelElem and poppedLevelElem.right is not None:
          levelArr.append(poppedLevelElem.right)
        elif poppedLevelElem and poppedLevelElem.right is None:
          levelArr.append(None)
      if len(levelArr) > 0:
        pushLevelArr = []
        for i in levelArr:
          if i:
            pushLevelArr.append(i.val)
          else:
            pushLevelArr.append(i)
        stack2.append(pushLevelArr)
        stack.append(levelArr)
    return stack2

def isSymmetric(root):
  if root is None:
    return 'yes'
  elif root.left is None and root.right is None:
    return 'yes'
  else:
    levelOrderArr = BFSTraversal2(root)
    print(levelOrderArr, 'level')
    for idx in range(1, len(levelOrderArr)):
      flag = False
      for idx2 in range(int(len(levelOrderArr[idx])/2)):
        if levelOrderArr[idx][idx2] != levelOrderArr[idx][len(levelOrderArr[idx])-idx2-1]:
          # print(levelOrderArr[idx2], idx2)
          flag = True
          break
      if flag:
        break
    if flag:
      return 'No'
    return 'Yes'
#  2nd way 
def isSymmetric2(root):
  if root is None:
    return 'yes'
  elif root.left is None and root.right is None:
    return 'yes'
  elif root.left is None or root.right is None:
    return 'No'
  else:
    leftNode = []
    rightNode = []
    if root.right.val == root.left.val:
      leftNode.append(root.left)
      rightNode.append(root.right)
    else:
      return False
    while len(leftNode) > 0 and len(rightNode) > 0:
      popl = leftNode.pop(0)
      popr = rightNode.pop(0)
      if popl.left and popr.right:
        if popl.left.val == popr.right.val:
          leftNode.append(popl.left)
          rightNode.append(popr.right)
        else:
          return False
      elif  popl.left or popr.right:
        return False
      if popl.right and popr.left:
        if popl.right.val == popr.left.val:
          leftNode.append(popl.right)
          rightNode.append(popr.left)
        else:
          return False
      elif  popl.right or popr.left:
        return False
    return True


# Code execution starts here 
if __name__=='__main__': 
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  # root.left.left = Node(3)
  # root.right.right = Node(4)
  print(isSymmetric2(root))