
# from collections import defaultdict
def topoSort(graph):
  visited = set()
  result = []

  def dfs(graph, node):
    visited.add(node)
    stack = [node]
    while stack:
      vertex = stack[len(stack)-1]
      # print(vertex, stack)
      flag = False
      for neighbour in graph[vertex]:
        if neighbour not in visited:
          flag = True
          stack.append(neighbour)
          visited.add(neighbour)
      if len(graph[vertex]) == 0 or not flag:
        result.append(stack.pop())



  for node in graph:
    if node not in visited:
      dfs(graph, node)
  print(result[::-1])






nodes = [3, 2], [3, 0], [2, 0], [2, 1]
graph = {
  4: [2, 3],
  2: [0, 1],
  3: [1],
  0: [],
  1: []
}
print(topoSort(graph))

# topo sort can only be applied to directed acyclic graph

# #  A vertex is pushed to stack only when all of its adjacent vertices (and their adjacent vertices and so on)
# , are already in stack.
# its time complexity is o(v+e)
#  if you want to process u then v must be processed..like files k compilatn
# agr ye dependent hnge kisi file pe toh pehle j dependent file h ideally
# wo process hna chhaye s ye h hta hai..work kis trrh process hna chahye..u , v where v must be
# processed frst then u
# stack me visualize
# u,
# v = > [v,u]
# v pehle process h then u but top sort me u upar ata h v se[its like reverse of work done]

# https://www.youtube.com/watch?v=6Vi5Td_a8B8
# dependency kind of sawal use topo

# higher dependent vertex should be at bottom of stack