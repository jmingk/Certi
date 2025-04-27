from collections import deque

N = 8
boxes = [3, 10, 5, 2, 8, 100, 7, 4]
max_value = 0

def dfs(index, a_last, b_last, a_sum, b_sum):
    global max_value

    if index == N:
        if a_sum > 0 and b_sum > 0:
            max_value = max(max_value, a_sum + b_sum)
        return

    current_box = boxes[index]

    # a_list에 넣기 (비었거나 비내림차순)
    if a_last is None or current_box >= a_last:
        dfs(index + 1, current_box, b_last, a_sum + current_box, b_sum)

    # b_list에 넣기 (비었거나 비오름차순)
    if b_last is None or current_box <= b_last:
        dfs(index + 1, a_last, current_box, a_sum, b_sum + current_box)

    # 아무 데도 안 넣기
    dfs(index + 1, a_last, b_last, a_sum, b_sum)


boxes.sort(reverse=True)
dfs(0, None, None, 0, 0)

print(max_value)