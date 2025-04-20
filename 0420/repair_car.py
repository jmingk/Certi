import sys
from collections import deque
sys.stdin = open("repair_input.txt", "r")
test_case = int(input())

for tc in range(1, test_case + 1):
    N, M, K, A, B = map(int, sys.stdin.readline().split())
    reception_time = list(map(int, sys.stdin.readline().split()))
    repair_time = list(map(int, sys.stdin.readline().split()))
    arrival_times = list(map(int, sys.stdin.readline().split()))

    reception_queue = deque()
    repair_queue = deque()
    reception_status = [0] * N
    repair_status = [0] * M
    reception_desk = [-1] * N
    repair_desk = [-1] * M
    time = 0
    processed = 0
    client_log = {}

    while processed < K:
        while arrival_times and arrival_times[0] == time:
            reception_queue.append(arrival_times.pop(0))

        for i in range(N):
            if reception_status[i] > 0:
                reception_status[i] -= 1
            if reception_status[i] == 0 and reception_queue:
                car = reception_queue.popleft()
                reception_status[i] = reception_time[i]
                repair_queue.append((car, time))
                reception_desk[i] = car
                client_log[car] = [i]

        for i in range(M):
            if repair_status[i] > 0:
                repair_status[i] -= 1
            if repair_status[i] == 0 and repair_queue:
                car, start_time = repair_queue.popleft()
                repair_status[i] = repair_time[i]
                processed += 1
                repair_desk[i] = car
                client_log[car].append(i)

        time += 1

    answer = sum(key + 1 for key, value in client_log.items() if value == [A - 1, B - 1])
    print(f"#{tc} {answer if answer > 0 else -1}")



# for _ in range(test_case):
#     N, M, K = map(int, sys.stdin.readline().split())
#     reception_time = list(map(int, sys.stdin.readline().split()))
#     repair_time = list(map(int, sys.stdin.readline().split()))
#     arrival_times = list(map(int, sys.stdin.readline().split()))
#
#     reception_queue = deque()
#     repair_queue = deque()
#     reception_status = [0] * N
#     repair_status = [0] * M
#     time = 0
#     processed = 0
#
#     while processed < K:
#         for i in range(N):
#             if reception_status[i] > 0:
#                 reception_status[i] -= 1
#             if reception_status[i] == 0 and reception_queue:
#                 car = reception_queue.popleft()
#                 reception_status[i] = reception_time[i]
#                 repair_queue.append((car, time))
#
#         for i in range(M):
#             if repair_status[i] > 0:
#                 repair_status[i] -= 1
#             if repair_status[i] == 0 and repair_queue:
#                 car, start_time = repair_queue.popleft()
#                 repair_status[i] = repair_time[i]
#                 processed += 1
#
#         while arrival_times and arrival_times[0] == time:
#             reception_queue.append(arrival_times.pop(0))
#
#         time += 1
#
#     print(time)
