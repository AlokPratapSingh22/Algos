
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def depth_first(graph: dict, source: chr):
    stack = [source]

    while stack:
        curr = stack.pop()
        print(curr, end='\t')
        stack.extend(graph[curr])
    print()


def depth_first_recurr(graph: dict, source: chr):
    print(source, end='\t')
    for neighbor in graph[source]:
        depth_first_recurr(neighbor)


def breadth_first(graph: dict, source: chr):
    queue = [source]

    while queue:
        curr = queue.pop(0)
        print(curr, end='\t')
        queue.extend(graph[curr])
    print()


depth_first(graph, 'a')
breadth_first(graph, 'a')
