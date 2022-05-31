def largest_comp(graph):
    visited = set()
    max_count = 0

    for node in graph:
        max_count = max(max_count, traverse(graph, node, visited))

    return max_count


def traverse(graph, node, visited) -> int:
    if node in visited:
        return 0

    visited.add(node)
    count = 1

    for neighbor in graph[node]:
        count += traverse(graph, neighbor, visited)

    return count


graph = {
    0: [8,  5],
    1: [4],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2, 1],
}

print(largest_comp(graph))
