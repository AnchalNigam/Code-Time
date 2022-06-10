from ctypes.wintypes import PINT


# graph = {
#   0: [1,2],
#   1: [2],
#   2: [3],
#   3: [],
#   4: [1]
# }
graph = {
  0: [1],
  1: [0],
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
    stack.append(node)
  for v in graph:
    if v not in visited:
      dfs(v)
  print(stack[::-1])
topoSort(graph)



#  A vertex is pushed to stack only when all of its adjacent vertices (and their adjacent vertices and so on)
# , are already in stack.
# its time complexity is o(v+e)
#  if you want to process u then v must be processed..like files k compilatn
# agr ye dependent hnge kisi file pe toh pehle j dependent file h ideally
# wo process hna chhaye s ye h hta hai..work kis trrh process hna chahye..u , v where v must be
# processed frst then u
# stack me visualize
# [u,
# v]
# v pehle process h then u but top sort me u upar ata h v se[its like reverse of work done]

# https://www.youtube.com/watch?v=6Vi5Td_a8B8
# dependency kind of sawal use topo

# higher dependent vertex should be at bottom of stack