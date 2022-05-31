def dfs(node: int, graph: dict[int: list[int]], visited: list[int], stack: list[int]):    
    visited.append(node)
    for neigh in graph[node]:
        if neigh not in visited:
            dfs(neigh, graph, visited, stack)
    stack.append(node)


def topo_sort_dfs(graph, n):
    visited = []
    stack = []
    for i in range(n):
        if i not in visited:
            dfs(i, graph, visited, stack)
    stack.reverse()
    print(stack)

# KAHN'S ALGO


def topo_sort_bfs(graph, n):
    # IN-DEGREE CALC
    in_degree = [0]*n
    for node in graph:
        for neigh in graph[node]:
            in_degree[neigh] += 1

    res = []

    # BFS
    q = []
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        node = q.pop(0)
        res.append(node)
        for neigh in graph[node]:
            if in_degree[neigh] > 0:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)
    print(res)


graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [0, 2]
}

topo_sort_dfs(graph, 6)
topo_sort_bfs(graph, 6)
