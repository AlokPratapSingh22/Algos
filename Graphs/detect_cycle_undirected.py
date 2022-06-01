# graph is represented by adjacency list: List[List[int]]
# DFS to detect cyclic
def is_cyclic_undirected_graph(graph):
    # set is used to mark visited vertices
    visited = set()

    def is_cyclic_recur(current_vertex, parent):
        # mark it visited
        visited.add(current_vertex)

        # Recur for all the vertices adjacent to current_vertex
        for v in graph[current_vertex]:
            # If the vertex is not visited then recurse on it
            if v not in visited:
                if is_cyclic_recur(v, current_vertex):
                    return True
            elif v != parent:
                # found a cycle
                return True

        return False

    # call recur for all vertices
    for u in range(len(graph)):
        # Don't recur for u if it is already visited
        if u not in visited:
            if is_cyclic_recur(u, -1):
                return True
    return False
