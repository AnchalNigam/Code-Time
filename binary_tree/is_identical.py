def isIdentical(root1, root2):
    # Code here
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    elif root1.data != root2.data:
        return False
    return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)