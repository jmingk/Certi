import sys
sys.stdin = open("0406/input.txt", "r")

import heapq
dx = [0,0,1,-1]
dy = [1,-1,0,0]
INF = int(1e9)

tc = 0
while True:
    N = int(input())
    if N == 0: break
    tc += 1
    mmap = []
    table = []

    for _ in range(N):
        mmap.append(list(map(int, input().split())))
        table.append([INF] * N)
    table[0][0] = mmap[0][0]

    q = [(table[0][0],0,0)]
    while q:
        now_cost, x, y = heapq.heappop(q)
        if table[x][y] < now_cost: continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx< N and 0<=ny<N):
                continue
            next_cost = now_cost + mmap[nx][ny]
            if table[nx][ny] <=  next_cost:
                continue
            table[nx][ny] = next_cost
            heapq.heappush(q, (next_cost, nx, ny))
    
    print("Problem " + str(tc) + ": " + str(table[N-1][N-1]))
        



