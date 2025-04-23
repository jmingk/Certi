N = 8
boxes = [3, 10, 5, 2, 8, 100, 7, 4]

max_value = 0

def dfs(index, a_list, b_list, a_sum, b_sum):
    global max_value

    if index == N-1:
        if a_list and b_list:
            max_value = max(max_value, a_sum + b_sum)
        return

    current_box = boxes[index]

    if not a_list or current_box >= a_list[-1]:
        dfs(index + 1, a_list + [current_box], b_list, a_sum + current_box, b_sum)

    if not b_list or current_box <= b_list[-1]:
        dfs(index + 1, a_list, b_list + [current_box], a_sum, b_sum + current_box)

    dfs(index + 1, a_list, b_list, a_sum, b_sum)

dfs(0, [], [], 0, 0)
print(max_value)