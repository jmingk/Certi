import sys
import copy

sys.stdin = open("cctv.txt", "r")

cctv_directions = {
    1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(-1, 0), (0, 1), (0, -1)], [(0, 1), (1, 0), (-1, 0)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (1, 0)]],
    5: [[(-1, 0), (1, 0), (0, 1), (0, -1)]]
}


def monitor_area(temp_map, x, y, directions):
    for dx, dy in directions:
        nx, ny = x, y

        while True:
            nx += dx
            ny += dy

            if nx < 0 or nx >= grid_rows or ny < 0 or ny >= grid_cols:
                break

            if temp_map[nx][ny] == 6:
                break

            if temp_map[nx][ny] == 0:
                temp_map[nx][ny] = -1


def dfs(depth, temp_map):
    global min_blind_spots

    if depth == len(cctvs):
        blind_spots = 0

        for row in temp_map:
            blind_spots += row.count(0)

        min_blind_spots = min(min_blind_spots, blind_spots)
        return

    x, y, cctv_type = cctvs[depth]

    for directions in cctv_directions[cctv_type]:
        new_map = [row[:] for row in temp_map]

        monitor_area(new_map, x, y, directions)

        dfs(depth + 1, new_map)


grid_rows, grid_cols = map(int, input().split())
office_map = []

for _ in range(grid_rows):
    row = list(map(int, input().split()))
    office_map.append(row)

cctvs = []

for x in range(grid_rows):
    for y in range(grid_cols):
        if 1 <= office_map[x][y] <= 5:
            cctvs.append((x, y, office_map[x][y]))

min_blind_spots = float('inf')

dfs(0, office_map)
print(min_blind_spots)