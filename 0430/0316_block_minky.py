import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input())

valid_blocks = [[2], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

for _ in range(T):
    max_height = -1
    blocks = list(map(int, input().split()))

    queue = deque()
    queue.append(([blocks[0]], 1, 1))

    while queue:
        current_blocks, current_height, idx = queue.popleft()

        if idx >= len(blocks):
            max_height = max(max_height, current_height)
            continue

        if current_blocks in valid_blocks:
            queue.append(([blocks[idx]], current_height + 1, idx + 1))

        if blocks[idx] in current_blocks:
            continue

        new_blocks = sorted(current_blocks + [blocks[idx]])
        queue.append((new_blocks, current_height, idx + 1))

    print(-1 if max_height == 1 else max_height)
