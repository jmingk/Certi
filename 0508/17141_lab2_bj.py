import sys
import copy
from itertools import combinations
from collections import deque

sys.stdin = open("lab.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(lab, virus_positions, N):
    queue = deque(virus_positions)
    visited = [[-1] * N for _ in range(N)]  # 방문 여부 및 시간 저장

    for r, c in virus_positions:
        visited[r][c] = 0

    max_time = 0

    while queue:
        r, c = queue.popleft()
        current_time = visited[r][c]

        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < N and lab[nr][nc] == 0 and visited[nr][nc] == -1:
                visited[nr][nc] = current_time + 1
                queue.append((nr, nc))
                max_time = max(max_time, current_time + 1)

    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0 and visited[i][j] == -1:
                return -1

    return max_time

def solve():
    virus_positions = []
    empty_count = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 2:
                virus_positions.append((i, j))
            elif lab[i][j] == 0:
                empty_count += 1

    if M > len(virus_positions):
        print(-1)
        return

    if empty_count == 0:
        print(0) # 빈 칸이 없으면 0 출력 후 종료
        return

    min_time = float("inf")

    for selected_virus in combinations(virus_positions, M):
        temp_lab = copy.deepcopy(lab)
        result = bfs(temp_lab, selected_virus, N)
        if result != -1:
            min_time = min(min_time, result)

    if min_time == float('inf'):
        print(-1)
    else:
        print(min_time)

N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

solve()