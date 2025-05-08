from collections import deque


def find_min_time():
    queue = deque()
    queue.append(start_pos)
    min_time[start_pos] = 0

    while queue:
        current_pos = queue.popleft()

        next_positions = [current_pos * 2, current_pos - 1, current_pos + 1]

        for next_pos in next_positions:
            if 0 <= next_pos <= max_limit:
                if next_pos == current_pos * 2:
                    new_time = min_time[current_pos]
                else:
                    new_time = min_time[current_pos] + 1

                if min_time[next_pos] > new_time:
                    min_time[next_pos] = new_time

                    if next_pos == current_pos * 2:
                        queue.appendleft(next_pos)
                    else:
                        queue.append(next_pos)


max_limit = 100000
start_pos, target_pos = map(int, input().split())
min_time = [float('inf')] * (max_limit + 1)

find_min_time()
print(min_time[target_pos])
