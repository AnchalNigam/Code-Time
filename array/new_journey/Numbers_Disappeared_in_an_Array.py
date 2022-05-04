def findDisappearedNumbers(nums):
  i = 0
  n = len(nums)
  while i < n:
    if (nums[i] != i+1):
      if(nums[nums[i]-1] == nums[i]):   
        i += 1
      else:
        temp = nums[i]
        nums[i] =  nums[nums[i]-1]
        nums[temp-1] = temp
    else:
      i += 1
  res = []
  for i in range(n):
    if nums[i] != i+1:
      res.append(i+1)
  return res
  

def findDisappearedNumbers(nums):
      i = 0
      n = len(nums)
      for i in range(n):
          temp = abs(nums[i])-1
          if(nums[temp] > 0):
              nums[temp] *= -1
      res = []
      for i in range(n):
          if nums[i] > 0:
              res.append(i+1)
      return res

# above solutn is applying cyclic sort knowledge -  basically as they said 1 to n h rhega
# toh har number k apne jagah pe pahuchao na..1 k 0th pe, 2 ko 1th index pe, 3 ko 2nd and so on
# so ab j apne jagah pe aajyange hai and last me iterate krke wrong places integer(i+1 se pta ag jaega) 
# which are at wrng
# ko consider kro


# below sol is new way of dealing ..smart way j mai toh nhi soch skte khud se..hehe
# for better explanatn refer here
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/344583/Python%3A-O(1)-space-solution
# main scene yahn ye kia gya ki number lo negate kro jo milta jaye and then j positive reh jaye mns whi hai