class Node:
  def __init__(self, data):
    self.left = None
    self.data = data
    self.right = None


def inorder(root):
  if root:
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
  if root:
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")
  
def preorder(root):
  if root:
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

# Code execution starts here 
if __name__=='__main__': 
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  inorder(root)
  print('\n')
  postorder(root)
  print('\n')
  preorder(root)


