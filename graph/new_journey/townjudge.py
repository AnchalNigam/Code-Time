from ast import List


class Solution:
    from collections import defaultdict
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        votes = [0] * (n+1)
        for _trust in trust:
            votes[_trust[0]] -= 1
            votes[_trust[1]] += 1
        for i in range(1, len(votes)):
            if votes[i] == n-1:
                return i
        return -1
        
# we have used indegree outdegree concept ki bhai jiska bhi trust hga usko ++ ar jisne kia uska
# -- kyunki wo candiate town judge k hga nhi because he has trusted someone so in this way 
# degrees maintain krke end me n-1 h gya toh town judge
