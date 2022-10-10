# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        sortedList = []
        def inorder(root):
            if root:
                inorder(root.left)
                sortedList.append(root.val)
                inorder(root.right)
     
        inorder(root)
        # print(sortedList)
        root = TreeNode()
        head = root
        for val in sortedList:
            node = TreeNode(val)
            root.right = node
            root = root.right
            # print(root.val)
        return head.right
# solve by own..here scene is we are storing sorted list and then making linkedlist using array
# here time and space complexity would be o(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.curr = TreeNode()
        temp = self.curr
        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            root.left = None
            self.curr.right = root
            self.curr = s
            inorder(root.right)
     
        inorder(root)
        return temp.right
# here main scene is change root.left and have temp copy of ypur ans that actually for sending
# root in ans because curr toh tail tak pahuch jaega..
# now see self.curr.right would be root and root ka left none kr do because left toh already travers
# krke neche tak aa gye hai inorder(root.left) se..fr ans me us node k atach kro fr root j traverse kr 
# rhe h like 1->2 se attach kr dia ab next me jana hai self.curr = self.curr.next krte h
# toh ab hme root j abhi tak tha like 3 attach h 4 k sath toh islie root k assign h jao
# taki 4 bhi travserse kro so aisa sa logic h see 
# https://leetcode.com/problems/increasing-order-search-tree/submissions/
# https://www.youtube.com/watch?v=6qHflItkcg0