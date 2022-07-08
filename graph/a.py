
n = 12
visited = set()
count = 0
edges = []
from collections import deque
from collections import defaultdict
graph=defaultdict(list)
for node1, node2 in edges:
    graph[node1].append(node2) 
def BFS(src):
  queue = deque()
 
  queue.append(src)

  # Assign Component Number
  visited.add(src)
  # Vector to store all the reachable
  # nodes from 'src'
  reachableNodes = 0
  #print("0:",visited)

  while (len(queue) > 0):
      
      # Dequeue a vertex from queue
      u = queue.popleft()

      reachableNodes += 1

      # Get all adjacent vertices of the dequeued
      # vertex u. If a adjacent has not been visited,
      # then mark it visited and enqueue it
      for itr in graph[u]:
          if itr not in visited:
              
              # Assign Component Number to all the
              # reachable nodes
              visited.add(itr)
              queue.append(itr)
 
  return reachableNodes


for node in range(n):
  # Visit all the nodes of the component
  if (node not in visited):
      print(BFS(node))
      count += (n-BFS(node))
print(count)