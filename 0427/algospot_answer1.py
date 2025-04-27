from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기값
dist = [[-1] * m for _ in range(n)]
dist[0][0] = 0

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    queue.appendleft((nx, ny))  # 빈 방이면 먼저
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))  # 벽이면 나중에

print(dist[n-1][m-1])
