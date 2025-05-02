# 백준 0427 연구소

import sys
from collections import deque
import copy
sys.stdin = open("test.txt", "r")

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

empty_spaces = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty_spaces.append((i, j))

virus_positions = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus_positions.append((i, j))

# print(empty_spaces)
# print(virus_positions)

def bfs():
    q = deque(virus_positions)
    temp_graph = copy.deepcopy(graph)
    while q:
        x, y = q.popleft()
        for z in range(4):
            nx, ny = x + dx[z], y + dy[z]
            if 0 <= nx < N and 0 <= ny < M and temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                q.append((nx, ny))

    return 0
#
# bfs()
L = len(empty_spaces)
print(L)
max_safe_area = 0
for i in range(L - 2):
    for j in range(i + 1, L - 1):
        for k in range(j + 1, L):
            make_wall = [empty_spaces[i], empty_spaces[j], empty_spaces[k]]
