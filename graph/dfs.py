def dfs(graph, root):
	visited = set()
	stack = [root]
	visited.add(root)

	while len(stack) != 0:
		vertex = stack.pop()
		print(vertex, 'vertex')
		for i in graph[vertex]:
			if i not in visited:
				visited.add(i)
				stack.append(i)

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
	dfs(graph, 'A')


# The time complexity of the DFS algorithm is represented in the form 
# of O(V + E), where V is the number of nodes and E is the number of edges.
# The space complexity of the algorithm is O(V).

