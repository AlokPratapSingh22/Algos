class DisjointSet:

    def __init__(self, rank=[], parent=[]) -> None:
        self.rank = rank
        self.parent = parent

    def makeSet(self, n: int):
        self.rank = [0]*n
        self.parent = [i for i in range(n)]

    def find(self, node: int) -> int:
        if node == self.parent[node]:
            return node

        # path compression
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u: int, v: int) -> int:
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

        # print(self.parent)
        return True
