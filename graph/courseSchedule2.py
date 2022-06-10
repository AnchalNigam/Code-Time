from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodesStatus = [0]*numCourses
        statusDic = {
            "DISCOVERING": 1,
            "UNVISITED": 0,
            "VISITED": 2
        }
        result = []
        graph=defaultdict(list)
        for node1, node2 in prerequisites:
            graph[node1].append(node2) 
        def isCyclic(node):
            stack = []
            stack.append(node)
            nodesStatus[node] = statusDic["DISCOVERING"]
            while stack:
                # print(queue)
                vertex = stack[len(stack)-1]
                if graph[vertex]:
                    neighbour = graph[vertex].pop()
                 
                    if nodesStatus[neighbour] == statusDic["DISCOVERING"]:
                        return True
                    elif nodesStatus[neighbour] == statusDic["UNVISITED"]:
                        stack.append(neighbour)
                        nodesStatus[neighbour] = statusDic["DISCOVERING"]
                else:
                    popedNode = stack.pop()
                    nodesStatus[popedNode] = statusDic["VISITED"]
                    result.append(popedNode)
                    
            return False
        for v in range(0, numCourses):
            if  nodesStatus[v] == statusDic["UNVISITED"]:
                if(isCyclic(v)):
                    return []
        return result

# same logic just we arestoring ans in result set...check course scheudle comments 

# recursion - bs stack k jagah recursion apna stack maintain kr rha hai thats it
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodeStatus = [0] * numCourses
        graph=defaultdict(list)
        for node1, node2 in prerequisites:
            graph[node1].append(node2) 
        result = []
        def isCyclic(node):
            nodeStatus[node] = 1 
            for neighbour in graph[node]:
                if nodeStatus[neighbour] == 0:                
                    if(isCyclic(neighbour)):
                        return True
                elif nodeStatus[neighbour] == 1:
                    return True

            nodeStatus[node] = 2
            result.append(node)
            return False
            
        for v in range(0, numCourses):
            if nodeStatus[v] == 0:
                if(isCyclic(v)):
                    return []
        return result
# no diff between this and courseschule1 just hme ek result array maintain krna pada bs
# time complexity whi o(v+e) -  space - auxiliary(recursion) - n -nodes, and node status - n, 2n