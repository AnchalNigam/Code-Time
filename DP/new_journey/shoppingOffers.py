from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.n = len(needs)
        self.dp = {}
        def solve(needs, start):
            print(needs, start, 'start')
            if start == len(special):
                res = 0
                for i in range(self.n):
                    res += needs[i]*price[i]
                print(res, 'ress')
                return res
                   
            if  (needs, start) in self.dp:
                return  self.dp[(needs, start)]
            flag = False
            for i in range(self.n):
                a = needs[i]-special[start][i]
                if a < 0:
                    flag = True
                    break
            accept = float('inf')
            needsTemp = needs
            if not flag:               
                for i in range(self.n):
                    b = list(needsTemp)
                    b[i] = b[i]-special[start][i]
                    needsTemp = tuple(b)
                print(needsTemp, 'needs')       
                accept = special[start][self.n] + solve(needsTemp, start)
            print(needs, 'needs2')
            reject = solve(needs, start+1)
            print(reject, accept, start, needs, 'test2')
            self.dp[(needs, start)] = min(accept, reject)
            return min(accept, reject)
        return solve(tuple(needs), 0)
            
                
                
# i learnt a lot from this...
# listen to solve problm using backtracking/dp..think of one entity[eg shopping offers]
# whether to take it or not...kya ise le bhi skte hai so
# us criteria k likho if (something something like in this we are checking any 
# entity should not come below 0) then take it and also compute answer by not taking
# then min of both...here make recursion tree for the same..it helps better in visualiztn
# here at last base case thda interestng tha usually we think..pura jab h jaega toh
# return 0 or something but here price k sath calc kia....now backtracking and
# isme ye diff hta ki hm res maintain krte hai ..here hm ans return krate rehte h at every step
# backtrack me end me we gather ans but here return return se ans banatae h
# isme memo ka jab socho toh check recursion and dynamic params usme h banaega memo
# and in this way memo kro dynamic param pe..interestng thing we should memo using
# array and dict