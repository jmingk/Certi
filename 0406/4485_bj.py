import heapq
import sys

INF = int(1e9)

def dijkstra(n, cave):
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = cave[0][0]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = [(cave[0][0], 0, 0)]
    heapq.heapify(q)

    while q:
        cost, x, y = heapq.heappop(q)

        if distance[x][y] < cost:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + cave[nx][ny]
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))
    return distance[n-1][n-1]

num = 1
while True:
    n = int(input())
    if n == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(n)]
    result = dijkstra(n, cave)
    print(f"Problem {num}: {result}")
    num += 1
