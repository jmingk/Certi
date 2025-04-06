#### 시간 초과 ....

import sys

def dijkstra(start, graph, n):
    distance = [sys.maxsize] * (n + 1)
    visited = [False] * (n + 1)
    distance[start] = 0

    for _ in range(n):
        min_dist = sys.maxsize
        min_node = -1

        for i in range(1, n + 1):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_node = i

        if min_node == -1:
            break

        visited[min_node] = True

        for next_node, cost in graph[min_node]:
            if not visited[next_node]:
                new_cost = distance[min_node] + cost
                if new_cost < distance[next_node]:
                    distance[next_node] = new_cost

    return distance

input_list = list(map(int, input().split()))  # 예: input_list = [4, 8, 2] -> n=4, m=8, x=2
n, m, x = input_list

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

max_distance = 0
for i in range(1, n + 1):
    go_distance = dijkstra(i, graph, n)[x]
    back_distance = dijkstra(x, graph, n)[i]
    max_distance = max(max_distance, go_distance + back_distance)

print(max_distance)
