from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        self.dp = {}
        def solve(start, res):
            if start == len(scores):
                return 0
            if (res, start) in self.dp:
                return self.dp[(res, start)] 
            
            flag = True
            for i in range(len(res)):
                score, age = res[i]
                # print(res[i], score, age)
                if age > ages[start] and score < scores[start] or (age < ages[start] 
                and score > scores[start]):
                    flag = False
                    # print('insidr')
                    break
            accept = float('-inf')
            resTemp = res
            # print(start, res, flag, 'uu')
            if flag:
                b = list(res)
                b.append((scores[start], ages[start]))
                resTemp = tuple(b)               
                accept = scores[start] + solve(start+1, resTemp)
            # print(res, start, accept, 'check')
            reject = solve(start+1, res)
            self.dp[(res, start)] =  max(reject, accept)
            return self.dp[(res, start)] 
        return solve(0, ())
        
                
                
                
        