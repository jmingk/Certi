from itertools import combinations
from collections import deque
import copy
import sys

sys.stdin = open("lab.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(lab, virus_positions):
    queue = deque(virus_positions)
    visited = [[-1] * M for _ in range(N)]

    for x, y in virus_positions:
        visited[x][y] = 0

    max_time = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
    return max_time


def solve():
    empty_spaces = []
    virus_positions = []

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                empty_spaces.append((i, j))
            elif lab[i][j] == 2:
                virus_positions.append((i, j))

    min_time = float('inf')

    for selected_virus in combinations(virus_positions, M):
        temp = copy.deepcopy(lab)
        result = bfs(temp, selected_virus)
        if result != -1:
            min_time = min(min_time, result)


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

solve()