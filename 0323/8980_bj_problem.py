# https://www.acmicpc.net/problem/8980
import sys
sys.stdin = open('8980_input.txt', 'r')

N, C = map(int, input().split())
M = int(input())
requests = []

for _ in range(M):
    start, end, boxes = map(int, input().split())
    requests.append([start, end, boxes])

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


