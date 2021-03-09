def moveZeroes(self, nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  start_idx = -1
  end_idx = 0
  for idx in range(len(nums)):
    if nums[idx] == 0:
      end_idx = idx
      if start_idx == -1:
        start_idx = idx
    elif start_idx != -1:
      nums[start_idx] = nums[idx]
      nums[idx] = 0
      start_idx += 1
      end_idx += 1