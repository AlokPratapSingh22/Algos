
def dfs(node, parent, graph, vis, tin, low, timer):
    vis.append(node)
    tin[node] = timer
    low[node] = timer
    timer += 1
    for neigh in graph[node]:
        if neigh == parent:
            continue

        if neigh not in vis:
            dfs(neigh, node, graph, vis, tin, low, timer)
            low[node] = min(low[node], low[neigh])

            if low[neigh] > tin[node]:
                print(neigh, " --- ", node)
        else:
            low[node] = min(low[node], tin[neigh])


def detect_bridge(graph, n):
    visited = []
    tin = [0]*(n+1)
    low = [0]*(n+1)

    timer = 0
    for i in range(1, n+1):
        if i not in visited:
            dfs(i, -1, graph, visited, tin, low, timer)


graph = {
    1: [2, 4],
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
    12: [10, 11]
}

detect_bridge(graph, 12)
