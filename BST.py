class Node:
  def __init__(self, data):
    self.left = None
    self.data = data
    self.right = None

def insert(root, node):
  if root is None:
    return root
  else:
    if node.data < root.data:
      if root.left is None:
        root.left = node
      else:
        insert(root.left, node)
    else:
      if root.right is None:
        root.right = node
      else:
        insert(root.right, node)


def inorder(root):
  if root:
    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)

def search(root, key):
  print(key, root.data)
  if root is None  or root.data == key:
    return root
  if key < root.data:
    return search(root.left, key)
  
  return search(root.right, key)

def minValuenNode(root):
  current = root
  while current.left is not None:
    current = current.left
  return current

def deleteNode(root, key):
  if root is None:
    return root
  if key < root.data:
    root.left = deleteNode(root.left, key)
  elif key > root.data:
    root.right = deleteNode(root.right, key)
  else:
    if root.right is None:
      temp = root.left
      root = None
      return temp
    if root.left is None:
      temp = root.right
      root = None
      return temp
    temp = minValuenNode(root.right)
    root.data = temp.data
    root.right = deleteNode(root.right, temp.data)
  return root

r = Node(50)
insert(r, Node(30))
insert(r, Node(40))
insert(r, Node(60))
insert(r, Node(10))
insert(r, Node(20))


# inorder(r)
# deleteNode(r, 30)
inorder(r)
# root = search(r, 30)
# print(root.data)
