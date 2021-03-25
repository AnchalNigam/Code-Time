def lengthOfLIS(self, nums: List[int]) -> int:
    i = 0
    j = i+1
    maxLen = 1
    lisc = [1 for idx in range(len(nums))]
    while j < len(nums):
        i = 0
        while i < j:               
            if nums[j] > nums[i] and lisc[j] <= lisc[i]:
                lisc[j] = 1+lisc[i]
                maxLen = max(maxLen, lisc[j])
            i += 1
        j += 1
    # print(lisc)
    return maxLen