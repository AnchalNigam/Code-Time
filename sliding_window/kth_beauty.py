class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        tempNum = str(num)
        start = 0
        end = 0
        n = len(tempNum)
        x = ""
        ans = 0
        while end < n:
            # print(start, end)
            x += tempNum[end]
           
            if (end-start) == k-1:
                temp = int(x)
                # print(temp)
                if temp != 0:
                    # print(temp)
                    ans += 1 if num%temp == 0 else 0
                # print(x)
                x = x[1:]
                # print(x, '***')
                start += 1
                    
            end += 1
        return ans
#solved using sliding window technique...see in this fixed size one , i faced that last tak 
# last wala calc kie bina end h ja rha tha ye sb issues i faced so i genralized template
# for sliding window ki frst do the work like x+=tempNum[end] then check whether that window
  # comes or not if yes then do further calc then move pointer, initially what i was doing,
  # x+=tempNum[end] i was writing after if condition, so whn pe i was wrong, frst 
  # do work then window check then end+=1 so ye h logic rkhna h for sliding window technique 
        
        