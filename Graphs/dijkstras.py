import heapq
import math

# Time complexity = O(E log(N))
# Space complexity = O(2N)


def shortest_path(graph: dict[int: list[tuple[int, int]]], source: int, N: int):
    dist = [math.inf]*(N+1)
    q = [(0, source)]
    heapq.heapify(q)
    dist[source] = 0
    while q:
        d, node = heapq.heappop(q)
        for neigh in graph[node]:
            newd = d+neigh[1]
            if newd < dist[neigh[0]]:
                dist[neigh[0]] = newd
                heapq.heappush(q, (newd, neigh[0]))

    for i in range(N+1):
        print(source, " -> ", i, dist[i])


graph = {
    1: [(2, 2), (4, 1)],
    2: [(1, 2), (5, 5), (3, 4)],
    3: [(4, 3), (5, 1), (2, 4)],
    4: [(1, 1), (3, 3)],
    5: [(2, 5), (3, 1)]
}

shortest_path(graph, 1, 5)
