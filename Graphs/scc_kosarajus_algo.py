def print_all_sccs(graph, n):

	# Step 1: Topological Sort
	stack = []
	visited = []
	
	def topo_dfs(i):		
		visited.append(i)
		for neigh in graph[i]:
			if neigh not in visited:				
				topo_dfs(neigh)
		stack.append(i)

	for i in range(n):
		if i not in visited:			
			topo_dfs(i)
	

	# Step 2: Transpose graph
	graph_t = {}
	
	for i in range(n):
		if i not in graph_t:
			graph_t[i] = []
		for neigh in graph[i]:
			if neigh not in graph_t:
				graph_t[neigh] = []
			graph_t[neigh].append(i)

	# Step 3: DFS
	vis = []
	
	def dfs(node, ans):
		vis.append(node)
		ans.append(node)
		for neigh in graph_t[node]:
			if neigh not in vis:				
				dfs(neigh, ans)
		

	while stack:
		node = stack.pop()
		if node not in vis:
			ans = []			
			dfs(node, ans)
			print(ans)			

graph={
	0: [1],
	1: [2,3],
	2: [0],
	3: [4],
	4: [],
}

print_all_sccs(graph, 5)
