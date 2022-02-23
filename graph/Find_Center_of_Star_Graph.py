from collections import defaultdict


def centerOfGraph(edges):
  graph = defaultdict(list)
  for node1, node2 in edges:
    graph[node1].append(node2)
    graph[node2].append(node1)
  allVertexVisit = len(graph.keys())-1
  for neighbour in graph:
    if len(graph[neighbour]) == allVertexVisit:
      return neighbour
  return False

edges = [[1,2],[5,1],[1,3],[1,4]]

print(centerOfGraph(edges))
    
# basic idea is single is accessible to every node that means array is eual to all (vertices-1)
    
      

