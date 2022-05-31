def shortest_path(graph, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        curr, dist = queue.pop(0)
        if curr == end:
            return dist
        if curr in visited:
            continue
        else:
            visited.add(curr)

        for neighbor in graph[curr]:

            queue.append((neighbor, dist+1))
    return -1


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


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

print(shortest_path(to_graph(edges), 'w', 'z'))
