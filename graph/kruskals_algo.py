# kruskals algo aaplies disjoin union set ds

# if we pick node that belong to diff compoents then we are maintianing no cycle thing and as in
# frst step we have to sort acc to weight toh ye mini maintain kr rha hai
# so in kruskals we frst sort then we pic node which are in diff components(same components makes
# cycle)

# time complexoty - MlogM+M*4alpha
# (frst mlogm is sorting and m*4alpha is your union disjoint set complexity which is 4aplha and 
# we are finding for all m nodes so m*4alpha which in total time complexity makes mlogm)
# space is pehle o(m) wo linear data struture me tuple of 3 elemns, o(n) for rank, o(n) for parent
# m is for tuple , n is for node asa sa kch concept h

# graph = { 
#   # (2, 1)- 1 is distance and 4 is node
#   1: [(1,4),(2,2),(4,5)],
#   2: [(3,3),(7,6),(3,4),(2,1)],
#   3: [(5,4),(8,6),(3,2)],
#   4: [(5,3),(3,2),(1,1),(9,5)],
#   5: [(9,4),(4,1)],
#   6: [(8,3),(7,2)]
# }

# graph = [(1,1,4),(2,1,2),(4,1,5),(3,2,3),(7,2,6),(3,2,4),(5,3,4),(8,3,6)
# ,(9,4,5)]

graph = [(1,7,6),(2,8,2),(2,6,5),(4,0,1),(4,2,5),(6,8,6),(7,2,3),(7,7,8),(8,0,7),(8,1,2),(9,3,4),(10,5,4),
(11,1,7),(14,3,5)]
def kruskalsAlgo(graph, n):
  graph.sort()
  parent = [i for i in range(n)]
  rank = [0]*(n)
  def union(u,v):
    u = findParent(u)
    v = findParent(v)
    if rank[u] < rank[v]:
      parent[u] = v
    elif rank[u] > rank[v]:
      # this means v gets connected to u so v ka parent ab u h gya thats why parent[v]=u
      parent[v] = u
    else:
      # (1,2) - 2 gets attached to 1 meaning parent of 2 becomes 1 and rank of 1 should inc
      parent[v] = u 
      rank[u] += 1
  def findParent(node):
    if(node == parent[node]):
      return node
    parent[node] = findParent(parent[node])
    return parent[node]
  costMst = 0
  mst = []
  for node in graph:
    w, u, v = node
    if findParent(u) != findParent(v):
      costMst += w
      mst.append(node)
      union(u, v)
  
  for i in mst:
    print(i)
    
 
print(kruskalsAlgo(graph, 9))
# if take we take from 1 nodes (not 0th index) then n+1 krte h for parent and rank vrna 0th se lete h
# why this parent[node]= findParent(parent[node]). if you check strivers video at last when
# (3,7) is picked then parent was [0,1,1,1,4,4,4,6].. so here 7 parent is 6 bt actually its parent is 4
# as 6 ka parent 4 hai so recursively apko 4 h milega so for next node lets say next node(_, 7) kuch ata h
# again recalcuatn se behtar h 7 k j response aya tha which was 4 save it in parent[node], parent[7]=4
# this is called compression ..so this is all about disjoint union set and rank and compression
