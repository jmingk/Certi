import sys
sys.stdin = open("0413/robot_cleaner.txt", "r")

N, M = map(int, input().split(' '))
r, c, dir = map(int, input().split(' '))
mmap = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
rev_dir = [2, 3, 0, 1]

UNCLEAN = 0
CLEAN = 2
WALL = 1
cleaned_cnt = 0

def print_map():
    for m in mmap:
        print(m)
    print()

def run(x, y, dir):
    global cleaned_cnt
    while True:
        print_map()
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if mmap[x][y] == UNCLEAN:
            mmap[x][y] = CLEAN
            cleaned_cnt += 1

        is_dirty = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if mmap[nx][ny] == UNCLEAN:
                is_dirty = True
                break
        
        # 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        if not is_dirty:
            x = x + dx[rev_dir[dir]]
            y = y + dy[rev_dir[dir]]
            if mmap[x][y] == WALL:
                return
            continue

        # 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
        # 반시계 방향으로 $90^\circ$ 회전한다.
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        else:
            for d in range(4):
                dir = (dir + 1) % 4
                
                nx = x + dx[dir]
                ny = y + dy[dir]
                if mmap[nx][ny] == UNCLEAN:
                    x = nx
                    y = ny
            continue

    return

for row in range(N):
    mmap.append(list(map(int, input().split())))

run(r,c, dir)

print(mmap)
print(cleaned_cnt)

