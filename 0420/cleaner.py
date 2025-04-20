# 첫째 줄에 방의 크기
# N과
# M이 입력된다.
# (3 \le N, M \le 50) 둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표
# (r, c)와 처음에 로봇 청소기가 바라보는 방향
# d가 입력된다.
# d가
# 0인 경우 북쪽,
# 1인 경우 동쪽,
# 2인 경우 남쪽,
# 3인 경우 서쪽을 바라보고 있는 것이다.
import sys
sys.stdin = open("cleaner_input.txt", "r")


# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 입력 처리
n, m = map(int, sys.stdin.readline().split())  # 방 크기
x, y, direction = map(int, sys.stdin.readline().split())  # 로봇 위치 및 방향
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 방 정보

clean_count = 0

def can_clean(x, y):
    return 0 <= x < n and 0 <= y < m and room[x][y] == 0

def find_left_direction(current_dir):
    return (current_dir - 1) % 4

def find_back_direction(current_dir):
    return (current_dir + 2) % 4  # 반대 방향

while True:
    # 현재 위치 청소
    if room[x][y] == 0:
        clean_count += 1
        room[x][y] = 2  # 청소 완료 표시

    moved = False
    for _ in range(4):
        direction = find_left_direction(direction)
        nx, ny = x + dx[direction], y + dy[direction]

        if can_clean(nx, ny):
            x, y = nx, ny
            moved = True
            break

    if not moved:
        back_dir = find_back_direction(direction)
        bx, by = x + dx[back_dir], y + dy[back_dir]

        if room[bx][by] == 1:  # 벽이면 작동 종료
            break
        else:
            x, y = bx, by  # 후진

print(clean_count)


#
# # 북, 동, 남, 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# n, m = map(int, sys.stdin.readline().split())  # 방 크기
# x, y, direction = map(int, sys.stdin.readline().split())  # 로봇 위치 및 방향
# room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 방 정보
#
# clean_count = 0
# def can_clean(x, y, room):
#     return room[x][y] == 0
#
#
# def find_left_direction(current_dir):
#     return (current_dir - 1) % 4
#
#
# def find_back_direction(current_dir):
#     return (current_dir + 2) % 4  # 반대 방향
#
#
# while True:
#     if room[x][y] == 0:
#         clean_count += 1
#         room[x][y] = 2
#
#     moved = False
#     for _ in range(4):
#         direction = find_left_direction(direction)
#         nx, ny = x + dx[direction], y + dy[direction]
#
#         if can_clean(nx, ny, room):
#             x, y = nx, ny
#             moved = True
#             break
#
#     if not moved:
#         back_dir = find_back_direction(direction)
#         bx, by = x + dx[back_dir], y + dy[back_dir]
#
#         if room[bx][by] == 1:
#             break
#         else:
#             x, y = bx, by
#
# print(clean_count)
#
#


