import queue

# Binary TreeNode class
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftView(root) :

    # write your code here
    res = []
    maxDepth = float('-inf')
    def leftViewPrint(root, depth):
        nonlocal maxDepth
        if root:
            if depth > maxDepth:
                maxDepth = depth
                res.append(root.data)
            leftViewPrint(root.left, depth+1)
            leftViewPrint(root.right, depth+1)
    leftViewPrint(root, 0)
    # print(res)
    print(' '. join(map(str, res)))


# i did it yoo..main focus ye tha ki mai ahr node k depth maintain krun toh receursion m jaise har
# picture pe arguement me pass krke data maintain krte h wo kia..ar agr depth se maxdepth jyda h
# mns usse jyda maxdepth tk gye h hm toh ignore ar ni gye toh mns left view me aya hga
# ye basic idea tha
# 