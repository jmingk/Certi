from collections import deque

M, N = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = 0

    while q:
        x, y, broken = q.popleft()

        if x == N - 1 and y == M - 1:
            return broken

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                new_broken = broken + maze[nx][ny]

                if visited[nx][ny] == 0 or new_broken < visited[nx][ny]:
                    visited[nx][ny] = new_broken
                    if maze[nx][ny] == 0:
                        q.appendleft((nx, ny, new_broken))
                    else:
                        q.append((nx, ny, new_broken))

print(bfs())
