import sys
sys.stdin = open("0406/input.txt", "r")

import heapq

N, M, X = map(int, input().split(' '))
INF = int(1e9)

def dijk(start):
    table = [INF] * (N + 1)
    table[start] = 0

    q = []
    heapq.heappush(q, [table[start], start])
    while q:
        _, node = heapq.heappop(q)
        for nnode in graph[node]:
            nextnode, dist = nnode
            if table[nextnode] > table[node] + dist:
                table[nextnode] =  table[node] + dist
                heapq.heappush(q, [table[nextnode], nextnode])
    return table

graph = dict()
for _ in range(M):
    src, dest, dist = map(int, input().split(' '))
    if src in graph:
        graph[src].append([dest, dist])
    else:
        graph[src] = [[dest, dist]]

dists = [0] * (N + 1)
for i in range(1, N + 1):
    table = dijk(i)
    dists[i] = table[X]

table = dijk(X)
for i in range(1, N + 1):
    dists[i] += table[i]

print(max(dists))


