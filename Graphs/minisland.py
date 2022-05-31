import math


def min_island(graph: list[chr, chr]):
    r = len(graph)
    c = len(graph[0])

    visited = set()
    min_count = math.inf
    for i in range(r):
        for j in range(c):
            count = explore(graph, i, j, visited)
            if count == 0:
                continue
            min_count = min(min_count, count)
    return min_count


def max_island(graph: list[chr, chr]):
    r = len(graph)
    c = len(graph[0])

    visited = set()
    max_count = 0
    for i in range(r):
        for j in range(c):
            count = explore(graph, i, j, visited)
            max_count = max(max_count, count)
    return max_count


def explore(graph: list, r, c, visited: set) -> bool:

    row_bounds = 0 <= r < len(graph)
    col_bounds = 0 <= c < len(graph[0])

    if not row_bounds or not col_bounds:
        return 0

    if graph[r][c] == 0:
        return 0

    curr = (r, c)
    if curr in visited:
        return 0

    visited.add(curr)

    count = 1

    count += explore(graph, r-1, c, visited)
    count += explore(graph, r+1, c, visited)
    count += explore(graph, r, c-1, visited)
    count += explore(graph, r, c+1, visited)

    return count


graph = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]

print(max_island(graph))
