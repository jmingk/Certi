import sys
import heapq

r = sys.stdin.readline

def dijkstra(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

for _ in range(int(r())):
    n, d, c = map(int, r().split())
    queue = []
    graph = {}
    for _ in range(d):
        a, b, s = map(int, r().split())
        if b not in graph.keys():
            graph[b] = {a : s}
        else:
            graph[b][a] = s

    for j in [v for v in range(1, n+1) if v not in graph.keys()]:
        graph[j] = {}

    prior_queue = dijkstra(graph, c)
    computers = [v for v in prior_queue.values() if v != float('inf')]
    print(len(computers), max(computers))