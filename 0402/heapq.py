import sys
import heapq

sys.stdin = open("input.txt", "r")

INF = int(1e9)

options = list(map(int, input().split()))
n, m, start = options[0], options[1], options[2]

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
def dijkstra(start, graph, n):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

    return distance

shortest_distances = dijkstra(start, graph, n)

for i in range(1, n + 1):
    print(shortest_distances[i])