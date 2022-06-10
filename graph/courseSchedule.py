from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      visited = set()
      dfsVisit = set()
      graph=defaultdict(list)
      for node1, node2 in prerequisites:
          graph[node1].append(node2) 
      def isCyclic(node):
          stack = []
          stack.append(node)
          while stack:
              # print(queue)
              vertex = stack[len(stack)-1]
              visited.add(vertex)
              dfsVisit.add(vertex)
              flag = False
              # print(vertex, 'vertex')
              for neighbour in graph[vertex]:
                  # print(neighbour, visited)
                  if neighbour not in visited:
                      flag = True
                      stack.append(neighbour)
                  # print(neighbour in visited, visited, neighbour)
                  elif neighbour in dfsVisit:
                      return True
              if len(graph[vertex]) == 0 or not flag:
                  dfsVisit.remove(stack.pop())
          return False
      for v in range(0, numCourses):
          if v not in visited:
              if(isCyclic(v)):
                  return False
      return True

# above scene gets failed when i was doing course schedule ii, but in course schedule its gets passed
# course schedle ii it gets failed when many nodes are dependent on 1 node mostly like 2 depends
# on 3 and 4 depends on 3 again, so isme stack me duplicate 3 append h ja rhe the which was not right


# next sol iteratve one is developed below
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodeStatus = [0] * numCourses
        graph=defaultdict(list)
        for node1, node2 in prerequisites:
            graph[node1].append(node2) 
        def isCyclic(node):
            stack = []
            stack.append(node)
            nodeStatus[node] = 1 
            #1 discovering, 0 unvisited, 2 visited
            while stack:
                # print(queue)
                vertex = stack[len(stack)-1]
                if graph[vertex]:
                    neighbour = graph[vertex].pop()
                    if nodeStatus[neighbour] == 1:
                        return True
                    elif nodeStatus[neighbour] == 0:
                        stack.append(neighbour)
                        nodeStatus[neighbour] = 1
                else:
                    popedNode = stack.pop()
                    nodeStatus[popedNode] = 2
            return False
        for v in range(0, numCourses):
            if nodeStatus[v] == 0:
                if(isCyclic(v)):
                    return False
        return True
# this one is interestng, here instead of making two sets, visited an dfs visit, one is there
# 0 is for visited, 1 is for discovered, 2 is fo visited...so we know topo me kya hta h j 
# sbse dependent hta hai matlb jispe sbse jyda dependency hte h wo stack me last hta hai..matlb
# frst elem...simple sa yad rkhna hau...jispe sb depedent h then usko h process krna pehle banta hai
# islie wo frst hte hai...ar ye dependency k chain hm dekhte rhnge using dfs..whhen there is no
# dependency at that node then stop and process it ..so here we are picking one node and process
# its neighbours[us node k process completely tab mana jaega when its dependents gets processed
# so will go to next neighbour, interstn thing we are popping the neighbor that gets processed and 
# pushed in stack[here above method gets differed wo duplicacy k issue resolve h gya is concept se]
# and making itdiscovered ..so jab koi us node ka dependent na rhega toh will pop it from stack
# and making its status visited...interestng way - 0(v+e) - all vertex + edges we ae exploring


# recursive approach - stack k replace kr dia auxiliary stack se
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodeStatus = [0] * numCourses
        graph=defaultdict(list)
        for node1, node2 in prerequisites:
            graph[node1].append(node2) 
        def isCyclic(node):
            nodeStatus[node] = 1 
            for neighbour in graph[node]:
                if nodeStatus[neighbour] == 0:                
                    if(isCyclic(neighbour)):
                        return True
                elif nodeStatus[neighbour] == 1:
                    return True

            nodeStatus[node] = 2
            return False
            
        for v in range(0, numCourses):
            if nodeStatus[v] == 0:
                if(isCyclic(v)):
                    return False
        return True