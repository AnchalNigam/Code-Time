def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
  if len(nums) == 0:
      return
  mid = len(nums)//2
  root = TreeNode(nums[mid])
  root.left = self.sortedArrayToBST(nums[:mid])
  root.right = self.sortedArrayToBST(nums[mid:])
  
  return root
  
# time complexity o(n) , space as stack me left rigt ja rha hai acc to height o(log(n))