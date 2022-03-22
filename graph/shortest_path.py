from dis import dis


graph = {
  0: [1,3],
  1: [2,0],
  2: [1],
  3: [0,4,7],
  4: [5,6,7,3],
  5: [4, 6],
  6: [5,4,7],
  7: [4,3,6]
}
def shortestPath(graph, source, dest, nodes):
  visited = set()
  queue = []
  distance = [float('inf') for i in range(nodes)]
  queue.append(source)
  distance[source] = 0
  while queue:
    vertex = queue.pop(0)
    visited.add(vertex)
    for neighbour in graph[vertex]:
      newD = distance[vertex] + 1
      distance[neighbour] = min(distance[neighbour], newD)
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)
  return distance[dest]

print(shortestPath(graph, 3, 7, 8))


# time complexity = O(V+E)
# space = O(N)+O(N)+O(N) - one for queue, one for distance and one for viisted

# here the basic idea is to make dist[src] = 0 as start and end is same
# then for next node, see its source node which is d[vertex] whatever is distance till this d[vertex]+1 
# is one way to reach that childnode so compare it with d[childnode] = min(d[childnode], d[vertex+1)
# in this way whole scenario is carried out, bfs