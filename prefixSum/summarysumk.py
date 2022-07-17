
from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        summation = 0
        count = 0
        dic[0] = 1
        for num in nums:
            summation += num
            if dic[summation-k]:
                count += dic[summation-k]
            if dic[summation]:
                dic[summation] = 1
            else:
                dic[summation] += 1
          
        return count

# eg [1,1,1]
# i learned vey interestng thing like if are at index 3 and sum = 3 then check sum-k kya
# already dic me hai if yes that means ki k bhi exist krega h so ye logic lagaya gya h
# inerstng thing is count += dic[summation-k]..here we need to check kite bar wo
# sum-k aya hai usko h add krna ..suppose ek bada array h usme do subsary ka sum 10 aa rha hai
# so we will count both so wo 10 ka count already hmne dic me maintain kia h hai toh hm
# usko h use krke add kr denge..for better understanding watch 10 as sum ka scene in
# this video https://www.youtube.com/watch?v=20v8zSo2v18
# time compelecity - o(n), space = o(distinct chars), worst case -o(n)