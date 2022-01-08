def maxProductSubarray(nums):
  maxProduct = 1
  minProduct = 1
  product1 = 1
  product2 = 1
  maxO = float('-inf')
  for idx in range(len(nums)):     
      x = max(nums[idx], nums[idx]*maxProduct, nums[idx]*minProduct)
      y = min(nums[idx], nums[idx]*maxProduct, nums[idx]*minProduct)
      maxProduct, minProduct = x, y
      
      
      maxO = max(maxProduct, maxO)

  return maxO


# You have three choices to make at any position in array.

# You can get maximum product by multiplying the current element with
# maximum product calculated so far. (might work when current
# element is positive).
# You can get maximum product by multiplying the current element with
# minimum product calculated so far. (might work when current
# element is negative).
# Current element might be a starting position for maximum product sub
# array


# https://leetcode.com/problems/maximum-product-subarray/discuss/48276/Python-solution-with-detailed-explanation