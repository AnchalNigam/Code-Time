def tripletSumToZero(nums):
  nums.sort()
  # print(nums)
  n = len(nums)
  count = 0
  res = []
  i = 0
  while i < n:          
      leftSum = 0-nums[i]
      # print(leftSum, 'LE')
      if i > 0 and nums[i] == nums[i-1]:
          # print('yes', i)
          i += 1
          continue
      l = i+1
      r = n-1
      subRes = [nums[i]]
      # print(subRes, 'sub')
      while l < r:
          if l > i+1 and nums[l] == nums[l-1]:
              # print('yes', i)
              l += 1
              continue
          summation = nums[l] + nums[r]
          if summation < leftSum:
              l += 1
          elif summation > leftSum:
              r -= 1
          else:
              # print(leftSum,l,r, 'leftsum')
              subRes.extend([nums[l], nums[r]])
              res.append(subRes)
              subRes = [nums[i]]
              l += 1
              r -= 1
      i += 1
  return res
  






nums = [-5, 2, -1, -2, 3]
print(tripletSumToZero(nums))


# in this main idea is to loop throigh 1 to n and use two sum logic after sorting
# to avoid duplicates...if we have choosen 1 obvio all two other sum will be found 
# and again 1 mila it means wo shorter window mw whi chesz dhudhenga which can lead to duplicates
# so skip that element using continue wala logic - o(n2)