import heapq
import math


class Node:
    def __init__(self, v=0, w=0) -> None:
        self.val = v
        self.weight = w

    def getVal(self):
        return self.val

    def getWeight(self):
        return self.weight


# Time commplexity greater than O(n^2)


def prims_brute(graph, N):
    # creating the required three arrays
    key = [math.inf]*N
    key[0] = 0
    mstSet = [False]*N
    parent = [-1]*N

    # as we require N-1 edges
    for _ in range(N-1):
        mini = math.inf
        u = 0
        # get the min value
        for v in range(N):
            if not mstSet[v] and key[v] < mini:
                mini = key[v]
                u = v

        mstSet[u] = True

        # for each neighbor or child update parent and weight
        for it in graph[u]:
            if mstSet[it.getVal()] == False and it.getWeight() < key[it.getVal()]:
                parent[it.getVal()] = u
                key[it.getVal()] = it.getWeight()

    print(0)
    for i in range(1, N):
        print(parent[i], " -> ", i)


def prims_algo(adj, N):

    mst = [False]*N
    parent = [-1]*N
    edges = [(w, 0, to) for to, w in adjl[0]]
    mst[0] = True
    heapq.heapify(edges)
    totalMst = 0
    while edges:
        wgt, st, to = heapq.heappop(edges)
        if not mst[to]:
            mst[to] = True
            parent[to] = st
            totalMst += wgt
            for to_next, w in adjl[to]:
                if not mst[to_next]:
                    heapq.heappush(edges, (w, to, to_next))

    print(parent, totalMst)


adj = {
    0: [Node(1, 2), Node(3, 6)],
    1: [Node(0, 2), Node(2, 3), Node(4, 5), Node(3, 8)],
    2: [Node(1, 3), Node(4, 7)],
    3: [Node(1, 8), Node(0, 6)],
    4: [Node(1, 5), Node(2, 7)]
}

adjl = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (4, 5), (3, 8)],
    2: [(1, 3), (4, 7)],
    3: [(1, 8), (0, 6)],
    4: [(1, 5), (2, 7)]
}
# prims_brute(adj, 5)
prims_algo(adjl, 5)
