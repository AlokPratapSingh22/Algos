from inspect import stack


def island_count(graph: list[chr, chr]):
    r = len(graph)
    c = len(graph[0])

    visited = set()
    count = 0
    for i in range(r):
        for j in range(c):
            if explore(graph, i, j, visited):
                count += 1
    return count


def explore(graph: list, r, c, visited: set) -> bool:

    row_bounds = 0 <= r < len(graph)
    col_bounds = 0 <= c < len(graph[0])

    if not row_bounds or not col_bounds:
        return False

    if graph[r][c] == 'W':
        return False

    curr = (r, c)
    if curr in visited:
        return False

    visited.add(curr)

    explore(graph, r-1, c, visited)
    explore(graph, r+1, c, visited)
    explore(graph, r, c-1, visited)
    explore(graph, r, c+1, visited)

    return True
