# Definition for a binary tree node.
from typing import Optional

# sol 1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = [0]
        def dfs(root, target):
            if root is None:
                return
            solve(root, target)
            dfs(root.left, target)
            dfs(root.right, target)
        def solve(root, target):
            if root is None:
                return
            # print(root.val, target)
            if (target-root.val) == 0:
                res[0] += 1 
            solve(root.left, target-root.val)
            solve(root.right, target-root.val)
        dfs(root, targetSum)
        return res[0]

# solution2
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = [0]
        dic = { 0 : 1 }
            
        def dfs(root, target):
            if root is None:
                return
            solve(root, target, 0)
       
        def solve(root, target, currPathSum):
            if root is None:
                return
            currPathSum += root.val
            if (currPathSum-target) in dic:
                # print('inside', currPathSum, dic)
                res[0] += dic[currPathSum-target]
            if currPathSum not in dic:
                dic[currPathSum] = 1
            else:
                dic[currPathSum] += 1
         
   
            solve(root.left, target, currPathSum)
            solve(root.right, target, currPathSum)
            if(dic[currPathSum]-1 == 0):
                del dic[currPathSum]
            else:
                dic[currPathSum] -= 1
        dfs(root, targetSum)
        return res[0]



# here above sol1 is actually using two loops concept..outer looop starts from 0 to n-1 and
# inner loop runs fromm i to last adn we add each num and checks if it equals to 0 ot not
# if yes then adding it to answer so in recursion, how to apply loop see above code sol1
# interstng na,,,,just use two calls to dfs(root.left), dfs(root.right)- this is loops basically
# and on each answer we are applying general path sum concept so this is done in o(n2) as its kind
# of two loops concept


# sol2 uses knowledge of Number of subarrays having sum exactly equal to k which uses hashmap
# https://www.youtube.com/watch?v=20v8zSo2v18. check this..initially intutn nhi aa rha tha
# mainly isme we maintain the sum so far and then - with target agr wo dic me mns wo sum previously
# kabhi exist kia tha meaning jis index pe exist kia tha whn se curr index is actual target
# so we used this concept and applied above sol
# interstng thing is if we are done with one root then we have to remove that root.val from dic
# so i removed using dic[currPathSum]-1 wale logic se as currPathsum h hga j remove krna hga
# interstng line which i was not able to write is  res[0] += dic[currPathSum-target]
# here what i understood is if that exist then how much it exist add that [frankly, utta palle na pada]