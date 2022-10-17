from collections import defaultdict
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        result = []
        def dfs(node, res):            
            res.append(node)
            if node == len(graph)-1:
                result.append(res[:])                
            else:
                for neighbour in graph[node]:
                    
                    dfs(neighbour, res)
    
                    res.pop()
        dfs(0, [])
        return result

    
            
            