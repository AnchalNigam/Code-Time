class Node:
  def __init__(self, data):
    self.left = None
    self.data = data
    self.right = None


def BFSTraversal(root):
  if root is None:
    return
  else:
    queue = []
    queue.append(root)
    while(len(queue) > 0):
      print(queue[0].data)
      node = queue.pop(0)
      if node.left is not None:
        queue.append(node.left)
      if node.right is not None:
        queue.append(node.right)

    
# Code execution starts here 
if __name__=='__main__': 
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  BFSTraversal(root)