class Node:
    def __init__(self, id: int) -> None:
        self.id = id
        self.adjacent = []


class Graph:

    def __init__(self, graph_dict=None) -> None:
        if graph_dict == None:
            self._nodeLookup = {}
        self._nodeLookup = graph_dict

    def edges(self, vertex):
        return self._nodeLookup[vertex]

    def all_vertices(self):
        return set(self._nodeLookup.keys())

    def all_edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self._nodeLookup:
            self._nodeLookup[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)

        vertex1, vertex2 = tuple(edge)

        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._nodeLookup:
                self._nodeLookup[x].add(y)
            else:
                self._nodeLookup[x] = [y]

    def __generate_edges(self):
        edges = []
        for vertex in self._nodeLookup:
            for neighbour in self._nodeLookup:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __iter__(self):
        self._iter_obj = iter(self._nodeLookup)
        return self._iter_obj

    def __next__(self):
        return next(self._iter_obj)

    def __str__(self) -> str:
        res = "vertices: "
        for k in self._nodeLookup:
            res += str(k)+" "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge)+" "
        return res


g = {
    'a': ['d'],
    'b': ['c'],
    'c': ['b', 'c', 'd', 'e'],
    'd': ['a', 'c'],
    'e': ['c'],
    'f': []
}

graph = Graph(g)
print(graph.all_vertices())
