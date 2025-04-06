import heapq

INF = int(1e9)

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

n, m = 6, 11
start = 1
graph = [[] for _ in range(n + 1)]
edges = [
    (1, 2, 2), (1, 3, 5), (1, 4, 1),
    (2, 3, 3), (2, 4, 2),
    (3, 2, 3), (3, 6, 5),
    (4, 3, 3), (4, 5, 1),
    (5, 3, 1), (5, 6, 2)
]

for a, b, c in edges:
    graph[a].append((b, c))

distance = dijkstra(start, graph, n)
for i in range(1, n + 1):
    print("INFINITY" if distance[i] == INF else distance[i])