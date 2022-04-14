from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
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
                res.append(nums[i])
        return res
      
# time complexity  - 0(n) , space -o(1). here main logic is put on as they have said 1 to n h honge number
# so cyclic sort lagaya gya k swapping us us number se kr do and last me iterate krke wrong places integer
# ko consider kro

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        dic = {}
        while i < len(nums):
            if (nums[i] != i+1):
                if(nums[nums[i]-1] == nums[i]):   
                    dic[nums[i]] = 1
                    i += 1
                else:
                    temp = nums[i]
                    nums[i] =  nums[nums[i]-1]
                    nums[temp-1] = temp
            else:
                i += 1
        return dic.keys()

# #time complexity  - 0(n) , space -o(n) as dic use hue.