import math

# Time complexity = O(NE)
# Space complexity = O(2N)


def shortest_path(graph, src, n):
    dist = [math.inf]*n

    edges = []
    for i in range(n):
        for neigh, wgt in graph[i]:
            edges.append((i, neigh, wgt))

    dist[src] = 0

    # running for n-1 times
    for _ in range(n-1):
        for u, v, wgt in edges:
            # Relaxing each edge
            if dist[u] + wgt < dist[v]:
                dist[v] = dist[u] + wgt

    # Checking for negative cycle
    for u, v, wgt in edges:
        if dist[u] + wgt < dist[v]:
            print('NEGATIVE CYCLE DETECTED')
            return

    for i in range(n):
        print(src, " --> ", i, " = ", dist[i])


graph = {
    0: [(1, 5)],
    1: [(2, -2), (5, -3)],
    2: [(4, 3)],
    3: [(4, -2), (2, 6)],
    4: [],
    5: [(3, 1)]
}

shortest_path(graph, 0, 6)
