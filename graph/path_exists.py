from collections import defaultdict

def PathExists(source, destination, edges):
  graph=defaultdict(list)
  queue=[]
  for node1,node2 in edges:
      graph[node1].append(node2)
      graph[node2].append(node1)
      
  queue.append(source)
  visited=set()
  while queue:
      currentNode=queue.pop(0)
      if currentNode==destination:
          return True
      visited.add(currentNode)
      for neighbor in graph[currentNode]:
          if neighbor not in visited:
              queue.append(neighbor)
  return False

edges=[[0,1],[1,2],[2,0]]
print(PathExists(0,2,edges))

# queue is BFS as whatever goes first we evualte it first..so breadth wise we are moving
# stack is DFS as last one is frstly we processing