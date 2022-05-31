def articulation_points(graph, n):
    vis = [0]*n
    tin = [0]*n
    low = [0]*n
    pts = set()

    def dfs(node, parent, timer):

        vis[node] = 1
        tin[node] = low[node] = timer
        timer += 1

        child = 0

        for neigh in graph[node]:
            if parent == neigh:
                continue

            if vis[neigh] == 0:
                dfs(neigh, node, timer)

                low[node] = min(low[node], low[neigh])
                if parent != -1 and low[neigh] >= tin[node]:
                    pts.add(node)
                child += 1
            else:
                low[node] = min(low[node], tin[neigh])

        if parent == -1 and child > 1:
            pts.add(node)

    timer = 0
    for i in range(n):

        if vis[i] == 0:
            dfs(i, -1, timer)

    print(pts)


graph = {
    0: [1, 13],
    1: [0, 2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 5],
    5: [4, 6],
    6: [7, 9],
    7: [6, 8],
    8: [7, 10, 9],
    9: [6, 8],
    10: [8, 11, 12],
    11: [10, 12],
    12: [10, 11],
    13: [0],
}

articulation_points(graph, 14)
