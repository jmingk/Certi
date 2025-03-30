import sys
sys.stdin = open("input.txt", "r")

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
        node = q.popleft()
        print(node, end=' ')
        if node not in graph.keys():
            continue
        for nnode in graph[node]:
            if nnode in visited:
                continue
            else:
                visited.add(nnode)
                q.append(nnode)
    return


N, M, V = map(int, input().split(' '))

graph = {}
for i in range(M):
    src, dest = list(map(int, input().split(' ')))
    if src not in graph.keys():
        graph[src] = [dest]
    else:
        graph[src].append(dest)
    if dest not in graph.keys():
        graph[dest] = [src]
    else:
        graph[dest].append(src)

for key in graph.keys():
    graph[key].sort()

# DFS
visited = set()
dfs(V)
print()

# BFS
visited = set([V])
bfs(V)
print()