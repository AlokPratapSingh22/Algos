def hasPath(graph: dict, src: chr, dst: chr) -> bool:
    if src == dst:
        return True

    for neighbor in graph[src]:
        return hasPath(graph, neighbor, dst)

    return False


def hadPath_bfs(graph: dict, src: chr, dst: chr) -> bool:
    queue = [src]

    while queue:
        curr = queue.pop(0)
        if curr == dst:
            return True
        queue.extend(graph[curr])
    return False


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print(hasPath(graph, 'a', 'f'))
