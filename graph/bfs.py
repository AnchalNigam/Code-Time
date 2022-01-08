def bfs(graph, root):
	visited = set()
	queue = [root]
	visited.add(root)

	while len(queue) != 0:
		vertex = queue.pop(0)
		print(vertex, 'vertex')
		for i in graph[vertex]:
			if i not in visited:
				visited.add(i)
				queue.append(i)

if __name__ == '__main__':
	graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

	print("Following is Breadth First Traversal: ")
	bfs(graph, 'A')

# https://www.programiz.com/dsa/graph-bfs

# Since all of ​the nodes and vertices are visited, 
# the time complexity for BFS on a graph is O(V + E)O(V+E);
#  where VV is the number of vertices and EE is the number of edges.

