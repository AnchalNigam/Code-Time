from ctypes.wintypes import PINT


graph = {
  0: [1,2],
  1: [2],
  2: [3],
  3: [],
  4: [1]
}
def topoSort(graph):
  visited = set()
  # queue = []
  stack = []
  def dfs(node):
    visited.add(node)
    for neighbour in graph[node]:
      if neighbour not in visited:
        dfs(neighbour)
  for v in graph:
    if v not in visited:
      dfs(v)
  print(stack[::-1])
topoSort(graph)



#  A vertex is pushed to stack only when all of its adjacent vertices (and their adjacent vertices and so on)
# , are already in stack.
# its time complexity is o(v+e)








