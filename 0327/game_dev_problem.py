import sys
import copy
sys.stdin = open("dev_game_input.txt", "r")

# map n x m 육지 or 바다 (3 <= N,M <= 50)
#동 서 남 북 중 한곳을 바라보고 시작
#현재 방향을 기준으로 왼(반시계)부터 차례대로 갈곳을 정함
#바로 왼쪽에 가보지 않은 칸이 존재 -> 왼쪽 한칸 전진 / 가봤으면 회전
#네 방향 다 가봤으면 바라보는 방향을 유지 한채 한칸 뒤로 -> 1단계 롤백 / 뒤쪽이 바다면 멈춤

#input_1 n m
#input_2 start (a, b) d ( 0:북 , 1:동, 2:남, 3:서)
#input_3 0:육지, 1:바다

#output 방문한 칸의 수 출력

import sys

sys.stdin = open("dev_game_input.txt", "r")

n, m = map(int, input().split())
a, b, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]

# Directions: 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# Initialize visit matrix
visit = [[0] * m for _ in range(n)]
visit[a][b] = 1

def turn_left(d):
    if d == 0:
        return 3
elif d == 1:
        return 0
elif d == 2:
        return 1
elif d == 3:
        return 2

count = 1
def move(a, b, d, count):
    for _ in range(4):
        d = turn_left(d)
        nx = a + dx[d]
        ny = b + dy[d]

        if visit[nx][ny] == 0 and game_map[nx][ny] == 0:
            visit[nx][ny] = 1
return move(nx, ny, d, count + 1)

    # All directions are either visited or sea
nx = a - dx[d]
    ny = b - dy[d]
    if game_map[nx][ny] == 0:
        return move(nx, ny, d, count)
    else:
        return count

# Start the recursive movement
count = move(a, b, d, 1)

print(count)