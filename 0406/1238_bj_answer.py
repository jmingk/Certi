import sys
sys.stdin = open("0406/input.txt", "r")

import heapq

N, M, X = map(int, input().split(' '))
INF = int(1e9)

def dijk(start, graph):
    distance = [INF] * (N + 1)
    distance[start] = 0

    heap = [[distance[start], start]]
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist: continue

        for nextnode, cost in graph[node]:
            if distance[nextnode] > dist + cost:
                distance[nextnode] =  dist + cost
                heapq.heappush(heap, [distance[nextnode], nextnode])
    return distance

graph = dict()
rev_graph = dict()
for _ in range(M):
    src, dest, dist = map(int, input().split(' '))
    if src in graph:
        graph[src].append([dest, dist])
    else:
        graph[src] = [[dest, dist]]
    if dest in rev_graph:
        rev_graph[dest].append([src, dist])
    else:
        rev_graph[dest] = [[src, dist]]

maxdist = 0
dist_toX = dijk(X, rev_graph)
dist_fromX = dijk(X, graph)

for i in range(1, N + 1):
    maxdist = max(maxdist, dist_toX[i] + dist_fromX[i])

print(maxdist)


