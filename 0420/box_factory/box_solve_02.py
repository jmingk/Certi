N = 8
boxes = [3, 10, 5, 2, 8, 100, 7, 4]

max_value = 0

def dfs(index, last_a, last_b, a_sum, b_sum):
    global max_value

    if index == N:
        if last_a is not None and last_b is not None:  # A와 B가 최소 1개 이상 선택된 경우만 유효
            max_value = max(max_value, a_sum + b_sum)
        return

    current_box = boxes[index]

    if last_a is None or current_box >= last_a:
        dfs(index + 1, current_box, last_b, a_sum + current_box, b_sum)

    if last_b is None or current_box <= last_b:
        dfs(index + 1, last_a, current_box, a_sum, b_sum + current_box)

    dfs(index + 1, last_a, last_b, a_sum, b_sum)

dfs(0, None, None, 0, 0)
print(max_value)


# max_value = 0
#
# def dfs(index, a_list, b_list, a_sum, b_sum):
#     global max_value
#
#     if index == N:
#         if a_list and b_list:
#             max_value = max(max_value, a_sum + b_sum)
#         return
#
#     current_box = boxes[index]
#
#     if not a_list or current_box >= a_list[-1]:
#         dfs(index + 1, a_list + [current_box], b_list, a_sum + current_box, b_sum)
#
#     if not b_list or current_box <= b_list[-1]:
#         dfs(index + 1, a_list, b_list + [current_box], a_sum, b_sum + current_box)
#
#     dfs(index + 1, a_list, b_list, a_sum, b_sum)
#
# dfs(0, [], [], 0, 0)
# print(max_value)