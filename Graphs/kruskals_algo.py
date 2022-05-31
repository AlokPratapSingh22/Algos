from disjoint_set import DisjointSet


def kruskals_algo(adj: list, N: int):
    adj.sort(key=lambda x: x[2])

    dj = DisjointSet()
    dj.makeSet(N)

    costMst = 0
    mst = []
    for node in adj:

        if dj.union(node[0], node[1]):
            mst.append(node)
            costMst += node[2]

    print(costMst)
    print(mst)


adj = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 3, 8),
    (1, 2, 3),
    (1, 4, 5),
    (2, 4, 7),
]

kruskals_algo(adj, 5)
