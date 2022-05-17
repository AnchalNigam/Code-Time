from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -(nums[i])
            dic = {}
            left = i+1
            right = n-1
            while left < right:
           
                if (nums[left] + nums[right]) == target:
                    # print(nums, nums[left], nums[right])
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left > right and nums[right] == nums[right-1]:
                        right -= 1                   
                    left += 1
                    right -= 1
                elif (nums[left] + nums[right]) < target:
                    left += 1
                else:
                    right -= 1
                
                    
        return result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = {}
        
        for i in range(n):
            target = -(nums[i])
            dic = {}
            for j in range(i+1, n):              
                if (target-(nums[j])) not in dic:
                    dic[nums[j]] = j
                else:
                    dic[nums[j]] = j
                    sortedTuple = sorted((nums[i], nums[j], target-nums[j]))
                    result[tuple(sortedTuple)] = 1
        finalRes = []            
        for key in result:
            finalRes.append(list(key))
        return finalRes
            
# below approach is using dic and then sorting it and then extractng the keys and then pshing
# space complexity high hai iska....time is o(n2)

# frst approach using sorting ad twi pointer....if any previous target is computed then
# obvio fr se compute krne ka sense nhi thats why  
# if i > 0 and nums[i] == nums[i-1]:
    # continue
# if pointers wale pe hai obvio agr apne left ka previous 0 hai suppose toh apne add kia last se
# target equal aa gye toh next 0 k compute krne k kya sense wo 0 k sath pair bana k kr lia hai 
# process thats why duplicate skip ..and skip krne k logic h ki supoose left and right dono
# me agr same value hnge toh duplicates aa jaynge agr diff hnge toh obvio apka same x can't make 
# target with diff y...agr 0 hai ar wo 2 k sath add hke target banaya toh ab ag right 3 h jaega aur left
# 0 rhega toh wo target thde bana payega islie bhi skip krna banta h ...because thats not possible
# same x se and diff y se target achieve hga,waise major skip duplicacy k avoid k lie banyaa gya hai
# so in this way it is solved...interesting skiping part