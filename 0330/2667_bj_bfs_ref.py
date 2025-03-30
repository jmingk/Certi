#bfs
import sys
sys.stdin = open("/workspaces/Certi/0330/2667_input.txt", "r")

from collections import deque

def bfs(graph, startx, starty, n):
    graph[startx][starty] = 0
    count = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([[startx,starty]])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:                
                count += 1
                q.append([nx, ny])
                graph[nx][ny] = 0
    return count

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]  # 지도 정보

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph, i, j, n))

result.sort()
print(len(result))
for size in result:
    print(size)
