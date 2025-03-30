# https://www.acmicpc.net/problem/8980
import sys
sys.stdin = open('8980_input.txt', 'r')

N, C = map(int, input().split())
M = int(input())
requests = []

for _ in range(M):
    start, end, boxes = map(int, input().split())
    requests.append([start, end, boxes])

# 도착지 기준으로 요청 정렬 (먼저 도착하는 요청을 우선 처리) // 검색
requests.sort(key=lambda x: x[1])

remaining_capacity = [C] * (N + 1)
total_boxes_delivered = 0

for start, end, boxes in requests:
    max_boxes_possible = C
    for village in range(start, end):
        max_boxes_possible = min(max_boxes_possible, remaining_capacity[village], boxes)
    for village in range(start, end):
        remaining_capacity[village] -= max_boxes_possible

    total_boxes_delivered += max_boxes_possible

print(total_boxes_delivered)

# 오답 // 15개 만 맞음   ==========================
# requests.sort()
# print(requests)
# truck = [0] * (N + 1)
# total_boxes = 0
# for start, end, boxes in requests:
#     print(max(truck[start:end]))
#     max_c = C - max(truck[start:end])
#     available = min(max_c, boxes)
#
#     for i in range(start, end):
#         truck[i] += available
#
#     total_boxes += available
#
# print(total_boxes)



