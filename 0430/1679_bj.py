from collections import deque

def bfs(n, k):
    visited = [0] * 100001
    queue = deque([(n, 0)])

    while queue:
        position, time = queue.popleft()

        if position == k:
            return time

        next_node = position - 1 # 한 칸 뒤
        if 0 <= next_node <= 100000 and not visited[next_node]:
            visited[next_node] = 1
            queue.append((next_node, time + 1))

        next_node = position + 1 # 한 칸 앞으로
        if 0 <= next_node <= 100000 and not visited[next_node]:
            visited[next_node] = 1
            queue.append((next_node, time + 1))

        next_node = position * 2 # 순간이동
        if 0 <= next_node <= 100000 and not visited[next_node]:
            visited[next_node] = 1
            queue.append((next_node, time + 1))

n, k = map(int, input().split())
print(bfs(n, k))
