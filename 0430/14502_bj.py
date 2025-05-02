from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread_virus(lab):
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                dfs(i, j, lab)

def dfs(x, y, lab):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
            lab[nx][ny] = 2
            dfs(nx, ny, lab)

def count_safe_area(lab):
    return sum(row.count(0) for row in lab)

def make_wall(wall_count):
    global max_safe_area

    if wall_count == 3:
        simulate_lab = deepcopy(lab)
        spread_virus(simulate_lab)
        max_safe_area = max(max_safe_area, count_safe_area(simulate_lab))
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(wall_count + 1)
                lab[i][j] = 0

def result():
    make_wall(0)
    print(max_safe_area)

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
max_safe_area = 0

result()