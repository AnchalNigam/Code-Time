class Solution(object):
  def firstMissingPositive(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      i = 0
      n = len(nums)
      while i < len(nums):
          correctIdx = nums[i]-1
          if correctIdx < (n) and nums[i] > 0 and nums[i] != nums[correctIdx]:
              nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
          else:
              i += 1
      # print(nums)
      ans = 1
      for i in range(i):
          if nums[i] == ans:
              ans += 1
      return ans
  

  # Here main scene was ki u have to find out frst positive integer which is
  #  basically starts from 1 ..matlb obvio 1 se jita length k array hga whn
  #  tak check kro agr 1 nhi h array me toh 1 hga else 1 to n sb h toh n+1 
  # hga meaning ek range dia tha hume and usme missing niklna tha so cyclic 
  # sort application….see below…awesome …which is negative we ignored which is 
  # greater than n ignored rest swap kr dia and check kia 1 h 2 h 3 4 h till n…cool sol
