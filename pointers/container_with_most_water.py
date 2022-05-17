from typing import List


class Solution:
  def maxArea(self, height: List[int]) -> int:
      left  = 0
      right = len(height)-1
      maxArea = float('-inf')
      while left < right:
          yAxis = min(height[left], height[right])
          area = yAxis * (right-left)
          maxArea = max(maxArea, area)
          if height[left] < height[right]:
              left += 1
          else:
              right -= 1
              
      return maxArea

# time complexity - 0(n) as in worst case scenario mid me jake answer suppose milta sp 
# major array ap traverse kr rhe h toh n hga....0(n) worst case
# two pointer and smary analysis of questn ki left and right k kaise kia jaye make me to solve
# this ques...yoo