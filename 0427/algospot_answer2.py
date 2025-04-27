import heapq

m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기화
dist = [[int(1e9)] * m for _ in range(n)]
dist[0][0] = 0

heap = []
heapq.heappush(heap, (0, 0, 0))  # (비용, x, y)

while heap:
    cost, x, y = heapq.heappop(heap)

    if dist[x][y] < cost:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            next_cost = cost + graph[nx][ny]
            if next_cost < dist[nx][ny]:
                dist[nx][ny] = next_cost
                heapq.heappush(heap, (next_cost, nx, ny))

print(dist[n-1][m-1])
