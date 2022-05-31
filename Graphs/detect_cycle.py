def checkCycle(node, graph, vis, dfsVis):
    vis.append(node)
    dfsVis.append(node)

    for n in graph[node]:
        if n not in vis:
            if checkCycle(n, graph, vis, dfsVis):
                return True
        elif n in dfsVis:
            return True
    dfsVis.remove(node)
    return False


def isCyclic_dfs(graph, n) -> bool:
    vis = []
    dfsVis = []

    for i in range(n):
        if i not in vis and i in graph:
            if checkCycle(i, graph, vis, dfsVis):
                return True
    return False


def isCyclic_bfs(graph, n):
    # IN-DEGREE CALC
    in_degree = [0]*n
    for node in graph:
        for neigh in graph[node]:
            in_degree[neigh] += 1

    # BFS
    q = []
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
    cnt = 0
    while q:
        node = q.pop(0)
        cnt += 1
        for neigh in graph[node]:
            in_degree[neigh] -= 1
            if in_degree[neigh] == 0:
                q.append(neigh)
    if cnt == n:
        return False
    return True


graph = {
    0: [8, 1, 5],
    1: [2],
    5: [8],
    6: [],
    7: [],
    8: [0],
    2: [3, 4],
    3: [4],
    4: [2],





}

print(isCyclic_dfs(graph, 9))
print(isCyclic_bfs(graph, 9))
