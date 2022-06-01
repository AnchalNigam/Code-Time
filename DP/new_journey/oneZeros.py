class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def counter(s):
            zeroCounter = 0
            oneCounter = 0
            for char in s:
                if char == "0":
                    zeroCounter += 1
                else:
                    oneCounter += 1
            return (zeroCounter, oneCounter)
        maxSubset = [0] 
        def solve(i, m, n, res):
            if i >= len(strs):
                maxSubset[0] = max(res, maxSubset[0])
                return
            
            
            
            m1, n1 = counter(strs[i])
            if m1 <= m and n1 <= n:
                solve(i+1, m-m1, n-n1, res+1)
            solve(i+1, m, n, res)
        solve(0, m, n, 0)
        return maxSubset[0]
            
            
            
      # in this i did it myself..main funda is backtracking use kia maine...2*n and space is o(n)
      # due to stack

# now memo iska krna hai then we have to think of single entity ..ek single elem k sath kya ka rhe h
# we are taking and not taking...we were not able to findout ans if we know the the previous
# two elem result so jab ye na h then think us single elem k sath kya h rha hai
# now with without answer nikalo,,, and return it and whatever params are changing unka h dp banao
# base case me kya answer return kre wo think..in this way memo
# time complexity - 0(len(str)*m*n) and space bi same + o(n) stack