def isBipartite_bfs(graph, N):
    colored = {}

    for i in range(N):
        if i not in colored and graph[i]:
            colored[i] = True
            queue = [i]

            while queue:
                node = queue.pop(0)

                for neigh in graph[node]:
                    if neigh not in colored:
                        colored[neigh] = not colored[node]
                        queue.append(neigh)
                    elif colored[neigh] == colored[node]:
                        return False
    return True
