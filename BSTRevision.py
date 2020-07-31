class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def createBST(root, newNode):
  if root is None:
    return root

  if newNode.data < root.data:
    if root.left is None:
      root.left = newNode
    else:
      createBST(root.left, newNode)
  else:
    if root.right is None:
      root.right = newNode
    else:
      createBST(root.right, newNode)
  

def preOrrderTraversal(root):
  if root:
    print(root.data)
    preOrrderTraversal(root.left)
    preOrrderTraversal(root.right)

def bfsTraversal(root):
  queue = []
  queue.append(root)
  while(len(queue) > 0):
    root = queue.pop(0)
    print(root.data, end=" ")
    if root.left is not None:
      queue.append(root.left)
    if root.right is not None:
      queue.append(root.right)
  

def InOrrderTraversal(root):
  if root:
    InOrrderTraversal(root.left)
    print(root.data)
    InOrrderTraversal(root.right)

def inOrderWithoutRecursion(root):
  queue = []
  current = root
  while True:
    if current is not None:
      queue.append(current)
      current = current.left
    elif(queue):
      current = queue.pop()
      print(current.data)
      current = current.right
    else:
      break

root = Node(4)
createBST(root, Node(5))
createBST(root, Node(2))
createBST(root, Node(1))
createBST(root, Node(3))
# preOrrderTraversal(root)
# bfsTraversal(root)
# InOrrderTraversal(root)
inOrderWithoutRecursion(root)