import sys
import copy
sys.stdin = open("past exam/0316/input.txt", "r")

from collections import deque

T = int(input())
# 1 3 2 3 2 3 1 1 3 1 3

# 가능한 경우 : [2],[1,2],[1,3],[2,3],[1,2,3]
possible_case = [[2],[1,2],[1,3],[2,3],[1,2,3]]
for test_case in range(T):
    max_level = -1
    blks = list(map(int, input().split(' ')))

    q = deque()
    q.append([[blks[0]], 1, 1])   # current floor, level, idx 
    while q:
        floor, level, idx = q.popleft()

        if idx >= len(blks):
            max_level = max(max_level, level)
            continue

        if floor in possible_case:
            q.append([[blks[idx]], level + 1, idx + 1])
        
        if blks[idx] in floor:
            continue
        else:
            floor.append(blks[idx])
            floor.sort()
            q.append([floor, level, idx + 1])
    
    if max_level == 1:
        print(-1)
    else:
        print(max_level)