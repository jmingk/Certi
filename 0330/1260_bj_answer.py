from collections import deque

def dfs(node):
    visited.add(node)
    print(node, end=' ')
    if node not in graph.keys():
        return
    for nnode in graph[node]:
        if nnode in visited:
            continue
        else:
            dfs(nnode)
    return

def bfs(start):
    q = deque([start])

    while q:
        node = q.pop()
        visited.add(node)
        print(node, end=' ')
        if node not in graph.keys():
            continue
        for nnode in graph[node]:
            if nnode in visited:
                continue
            else:
                q.append(node)

    return


N, M, V = list(map(int, input().split(' ')))

graph = {}
for i in range(M):
    src, dest = list(map(int, input().split(' ')))
    if src not in graph.keys():
        graph[src] = [dest]
    else:
        graph[src].append(dest)

# DFS
visited = set()
dfs(V)
print()

# BFS
visited = set()
bfs(V)
print()



print(graph)