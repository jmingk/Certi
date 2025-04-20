from collections import deque

box = [3, 10, 5, 2, 8, 100, 7, 4]
sum_list = []


def max_box_value(box):
    queue = deque(box)

    while queue:
        A = []
        B = []
        temp_queue = deque(queue) 

        while temp_queue:
            value = temp_queue.popleft()
            if not A or value > A[-1]:
                A.append(value)
            else:
                B.append(value)

        B.sort(reverse=True)
        sum_list.append(sum(A) + sum(B))

        queue.popleft()

    print(max(sum_list))


max_box_value(box)