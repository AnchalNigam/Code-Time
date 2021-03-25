 def majorityElement(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return -1
    candidateKey_idx = 0
    count = 1
    for idx in range(1, len(nums)):
        if nums[candidateKey_idx] == nums[idx]:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidateKey_idx = idx
            count = 1 
    count = 0
    for idx in range(len(nums)):
        if nums[idx] == nums[candidateKey_idx]:
            count += 1
        if (count) > len(nums)//2:
            return nums[candidateKey_idx]
    return -1

        
  print(-1)

# if alternate elements are same then update count if not then decrease count by 1
# and check if count is 0 then update candidate key and count= 1 else move