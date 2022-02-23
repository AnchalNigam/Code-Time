def isGraphBipartite(graph):
  from collections import defaultdict
  n = len(graph)
  queue = []
  
  colors = [-1 for i in range(n)]

  for nodes in range(n):
      if(colors[nodes] != -1):
          continue
      queue.append(nodes)
      colors[nodes] = 1
      while queue:
          vertex = queue.pop(0)
          for neighbour in graph[vertex]:
              if colors[neighbour] == -1:
                  colors[neighbour] = 1-colors[vertex]
                  queue.append(neighbour)
              elif colors[neighbour] == colors[vertex]:
                  return False
  return True
                    
# graph bipartite is that where adjacent nodes color is diff(lke if we painted node in green then its
# adacent should be blue) so here adjacent list ip is given meaning [[1,2,3],[0,2],[0,1,3],[0,2]] ...o 
# index mns 0 number node conexted to 1,2,3 whereas 1 numbered node is conected to 0, 2
# so we have not prepared our graph and put bfs search....if node is not colored then colored it
# opp to its parent node otherwise checked same color toh nhi....if yes retred false....
# why this loop? because its necessay to visit every node as some node can be isolated
# so visit every node then decide and whoever is visited continue - for this last statement check this
# example - [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
# here 0th node is isolated...
                    
                    
        