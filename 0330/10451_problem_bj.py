import sys

sys.stdin = open("10451_input.txt", "r")
test_case = int(input())

for _ in range(test_case):
    num = int(input())
    num_list = list(map(int, input().split()))
    num_sort = sorted(num_list)

    visited = [0] * num
    count = 0

    for i in range(num):
        if visited[i] == 0:
            current = i
            while visited[current] == 0:
                visited[current] = 1
                for j in range(num):
                    if num_list[j] == num_sort[current]:
                        current = j
                        break
            count += 1

    print(count)



