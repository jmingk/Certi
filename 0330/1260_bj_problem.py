from collections import deque


def dfs(graph, node, visited):
    visited.append(node)
    print(node, end=' ')
    for node in graph[node]:
        if node not in visited:
            dfs(graph, node, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    # visited 표시를 두번 해준다.
    # visited.append(start)
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for node in graph[current]:
            if node not in visited:
                visited.append(node)
                queue.append(node)


n, m, start = map(int, input().split())

graph = {}
# 만약 모든 노드에 대해 list를 만들고 시작하면 map 안써도 된다.
for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for key in graph:
    graph[key].sort()

visited_dfs = []
visited_bfs = []

dfs(graph, start, visited_dfs)
print()
visited_bfs.append(start)
bfs(graph, start, visited_bfs)