import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    heap = [(0, 0, 0)]
    visited[0][0] = 0

    while heap:
        broken, x, y = heapq.heappop(heap)

        if x == N - 1 and y == M - 1:
            return broken

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                new_broken = broken + maze[nx][ny]

                if visited[nx][ny] > new_broken:
                    visited[nx][ny] = new_broken
                    heapq.heappush(heap, (new_broken, nx, ny))

M, N = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]

print(dijkstra())