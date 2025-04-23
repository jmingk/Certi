from collections import deque

N = 8
boxes = [3, 10, 5, 2, 8, 100, 7, 4]

# sum_list = []
# max_value = 0
#
# boxes_deque = deque(boxes)
#
# while boxes_deque:
#     a_list = []
#     b_list = []
#     for box in boxes:
#         if not a_list or box >= a_list[-1]:
#             a_list.append(box)
#
#     remaining_boxes = [box for box in boxes if box not in a_list]
#     remaining_boxes.sort(reverse=True)
#     b_list = []
#
#     for box in remaining_boxes:
#         if not b_list or box <= b_list[-1]:
#             b_list.append(box)
#
#     total_sum = sum(a_list) + sum(b_list)
#     sum_list.append(total_sum)
#     max_value = max(max_value, total_sum)
#
# print(max_value)

# from collections import deque
#
# sum_list = []
# max_value = 0
#
# # 가능한 모든 A의 선택 범위를 탐색
# for a_end in range(1, N + 1):
#     a_list = []
#
#     # A의 선택: 오름차순 유지
#     for i in range(a_end):
#         if not a_list or boxes[i] >= a_list[-1]:
#             a_list.append(boxes[i])
#
#     # B의 선택: 남은 박스 중 내림차순 유지
#     remaining_boxes = boxes[a_end:]
#     b_list = []
#
#     for box in remaining_boxes:
#         if not b_list or box <= b_list[-1]:
#             b_list.append(box)
#
#     # 최댓값 계산
#     total_sum = sum(a_list) + sum(b_list)
#     sum_list.append(total_sum)
#     max_value = max(max_value, total_sum)
#
# print(max_value)


max_value = 0

def dfs(index, a_list, b_list):
    global max_value

    if index == N-1:
        if a_list and b_list:
            a_total = sum(a_list)
            b_total = sum(b_list)
            max_value = max(max_value, a_total + b_total)
        return

    current_box = boxes[index]

    if not a_list or current_box >= a_list[-1]:
        dfs(index + 1, a_list + [current_box], b_list)

    if not b_list or current_box <= b_list[-1]:
        dfs(index + 1, a_list, b_list + [current_box])

    dfs(index + 1, a_list, b_list)

boxes.sort(reverse=True)
dfs(0, [], [])

print(max_value)


