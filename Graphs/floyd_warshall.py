import math
import copy

# Time complexity = O(n^3)
# Space complexity = O(2*n^2)


def all_pair_shortest_path(adj, n):
    dist = [[math.inf for _ in range(n)] for __ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        for neigh, wgt in adj[i]:
            dist[i][neigh] = wgt

    for i in range(n):
        newD = copy.deepcopy(dist)
        for r in range(n):
            for c in range(n):
                if r == i or c == i:
                    continue

                newD[r][c] = min(dist[r][c], dist[r][i]+dist[i][c])

        dist = copy.deepcopy(newD)

    for row in dist:
        print(row)


adj = {
    0: [(1, 8), (3, 1)],
    1: [(2, 1)],
    2: [(0, 4)],
    3: [(2, 9), (1, 2)]
}

all_pair_shortest_path(adj, 4)
