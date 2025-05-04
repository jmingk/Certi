from itertools import combinations
from copy import deepcopy
import sys

sys.stdin = open("lab.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sum_area_spread(lab):
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                dfs(i, j, lab)

    return sum(row.count(0) for row in lab)

def dfs(x, y, lab):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
            lab[nx][ny] = 2
            dfs(nx, ny, lab)

def make_wall():
    empty_spaces = []
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                empty_spaces.append((i, j))
    max_safe_area = 0

    for make_walls in combinations(empty_spaces, 3):
        temp_lab = deepcopy(lab)
        #print(walls)
        for x, y in make_walls:
            temp_lab[x][y] = 1
        max_safe_area = max(max_safe_area, sum_area_spread(temp_lab))

    print(max_safe_area)

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

make_wall()


#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# #count_safe_area 와 spread_virus 함수 합치기
# def spread_virus(lab):
#     for i in range(N):
#         for j in range(M):
#             if lab[i][j] == 2:
#                 dfs(i, j, lab)
#
# def dfs(x, y, lab):
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#
#         if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
#             lab[nx][ny] = 2
#             dfs(nx, ny, lab)
#
# def count_safe_area(lab):
#     return sum(row.count(0) for row in lab)
#
# def make_wall(wall_count):
#     global max_safe_area
#
#     if wall_count == 3:
#         simulate_lab = deepcopy(lab)
#         spread_virus(simulate_lab)
#         max_safe_area = max(max_safe_area, count_safe_area(simulate_lab))
#         return
#
#     for i in range(N):
#         for j in range(M):
#             if lab[i][j] == 0:
#                 lab[i][j] = 1
#                 make_wall(wall_count + 1)
#                 lab[i][j] = 0
#
# def result():
#     make_wall(0)
#     print(max_safe_area)
#
# N, M = map(int, input().split())
# lab = [list(map(int, input().split())) for _ in range(N)]
# max_safe_area = 0
#
# result()