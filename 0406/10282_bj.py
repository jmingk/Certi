#### 오답========

import heapq
import sys

INF = int(1e9)

def dijkstra(n, graph, start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = [(0, start)]

    while q:
        time, now = heapq.heappop(q)
        if distance[now] < time:
            continue
        for next_node, cost in graph[now]:
            new_time = time + cost
            if new_time < distance[next_node]:
                distance[next_node] = new_time
                heapq.heappush(q, (new_time, next_node))

    return distance

t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[a].append((b, s))
    result = dijkstra(n, graph, c)
    infected_count = sum(1 for x in result if x != INF)
    max_time = max(x for x in result if x != INF)
    print(infected_count, max_time)
