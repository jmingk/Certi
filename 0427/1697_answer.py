import sys
sys.stdin = open("0427/input.txt", "rt")
import copy
from collections import deque

def print_map(mmap):
    for line in mmap:
        print(line)

N, M = map(int, input().split())
mmap = []
zeros = []
viruses = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 0:
            zeros.append([i,j])
        if line[j] == 2:
            viruses.append([i,j])
    mmap.append(line)

def bfs(start_virus, _map):
    q = deque([start_virus])
    dx, dy = [0,0,-1,1], [1,-1,0,0]

    while q:
        x, y = q.pop()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M :
                if _map[nx][ny] == 0:
                    _map[nx][ny] = 2

    return

def run_virus(added_walls):
    tmap = copy.deepcopy(mmap)
    for xy in added_walls:
        tmap[xy[0]][xy[1]] = 1
    
    for virus in viruses:
        bfs(virus, tmap)
    
    cnt = 0
    for zero in zeros:
        if tmap[zero[0]][zero[1]] == 0:
            cnt += 1
    
    return

def dfs(idx, selected):
    global zeros
    if len(selected) == 3:
        run_virus(selected)
        return
    
    if idx >= len(zeros):
        return
    dfs(idx + 1, selected)
    dfs(idx + 1, selected + [zeros[idx]])

    return

dfs(0, [])

print_map(mmap)





