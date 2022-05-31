def to_graph(edges):
    graph = {}

    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = [edge[1]]
        if edge[1] not in graph:
            graph[edge[1]] = [edge[0]]

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph


def has_path(graph, src, dst):
    visited = set()

    queue = [src]

    while queue:
        curr = queue.pop(0)
        if curr in visited:
            continue
        visited.add(curr)
        if curr == dst:
            return True
        queue.extend(graph[curr])
    return False


edges = [
    ['i', 'j'],
    ['j', 'k'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]

graph = to_graph(edges)
print(has_path(graph, 'i', 'o'))
