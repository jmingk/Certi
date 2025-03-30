#bfs
import sys
sys.stdin = open("/workspaces/Certi/0330/2667_input.txt", "r")

def bfs(graph, x, y, n):
    graph[x][y] = 0
    count = 1  # 현재 단지 크기
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            count += dfs(graph, nx, ny, n)
    return count

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]  # 지도 정보

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs()

    # arr = [0] + list(map(int, input().split()))
    # visited =[0 for _ in range(n+1)]
    # count = 0
    # for i in range(1, n + 1):
    #     if (visited[i]) == 0:
    #         continue
    #     node = i
    #     count += 1
    #     visited[node] = 1
    #     node = arr[node]
    #     # while :


    print(count)
