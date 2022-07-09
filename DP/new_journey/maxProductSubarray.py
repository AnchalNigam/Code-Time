class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = float('-inf')
        n = len(nums)
        product = 1
        for i in range(n):
            product *= nums[i]
            maxProduct = max(maxProduct, product)
            if nums[i] == 0:
                product = 1
        product = 1
        for i in range(n-1, -1, -1):
            product *= nums[i]
            maxProduct = max(maxProduct, product)
            if nums[i] == 0:
                product = 1
        return maxProduct
            
# interesting, not done by me..but watched pepcoding video - 
# https://www.youtube.com/watch?v=jzQ-f2uU0UU
# so here scene is obvio ya toh start se arr answer hga ya fr end se
# mid subaray kabhi na h skta - watch video for ans but mota mota ye scene 
# -ve -ve ane se + ka scene h islie start ya toh end wala scene h
