# minimum spanning tree is who is having n nodes and n-1 edges(it shuld not have cycle) 
# and if i add all edges
# it shuld be mimimum....

# implementation is pick one and find minimu of that edge and cehck cycle na h
# again pick min of all the edges through which you are coming..
# graph = { 
#   # (2, 1)- 1 is distance and 4 is node
#   0: [(2,1), (6,3)],
#   1: [(2,0), (5, 4), (3,2),(8,3)],
#   2: [(3,1),(7,4)],
#   3: [(6,0),(8,1)],
#   4: [(5,1),(7,2)],
# }

graph = { 
  # (2, 1)- 1 is distance and 4 is node
  1: [(1,4),(2,2),(4,5)],
  2: [(3,3),(7,6),(3,4),(2,1)],
  3: [(5,4),(8,6),(3,2)],
  4: [(5,3),(3,2),(1,1),(9,5)],
  5: [(9,4),(4,1)],
  6: [(8,3),(7,2)]
}
def minSpanningTree(graph,s, n):
  dis = [float('inf')] * (n+1)
  parent = [-1] * (n+1)
  unvisited_queue = [(0, s)]
  mst = set()
  dis[s] = 0
  import heapq
  heapq.heapify(unvisited_queue)
  while len(unvisited_queue) > 0:
    _, vertex = heapq.heappop(unvisited_queue)
    # print(vertex)
    if vertex in mst:
      continue
    mst.add(vertex)
    for neighbour in graph[vertex]:
      w, v = neighbour
      if v not in mst: 
        # print(v, w, 'checking')
        # newWeight = dis[vertex] + w
        if dis[v] > w:
          dis[v] = w
          heapq.heappush(unvisited_queue,(dis[v], v))    # see this dis[v] ye store krte h not w
          parent[v] = vertex

  print(parent, 'check')

minSpanningTree(graph, 1, 6)

# time complexity is (N+E)logn ...n is outer looop j hmne lagaya nhi..check is cyclic wala usme
# lagaya h basically agr graph break wala h toh usko consider k loie loop lgana chahye
# so n and e is inside for neighbour in vetex k lie loop and logn is for prioroty queue
# space is parent ka o(n), unvisted ka o(n), dis ka o(n)