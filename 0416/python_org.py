## dfs
# dfs list
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)

# dfs dict
def dfs_dict(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for n in graph[node]:
            dfs(graph, n, visited)

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end= " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# permutations

from itertools import permutations
arr = [1, 2, 3]
for perm in permutations(arr, 2):
    print(perm)

# 중복제거
arr_2 = [1, 2, 3, 2, 2, 3, 4, 4, 4, 5]
new_list = []

for num in arr_2:
    if num not in new_list:
        new_list.append(num)
print(new_list)