N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_result = float('-inf')
min_result = float('inf')

def dfs(index, current_result):
    global max_result, min_result
    if index == N:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:
                dfs(index + 1, current_result + numbers[index])
            elif i == 1:
                dfs(index + 1, current_result - numbers[index])
            elif i == 2:
                dfs(index + 1, current_result * numbers[index])
            elif i == 3:
                if numbers[index] != 0:
                    dfs(index + 1, int(current_result / numbers[index]))
            operators[i] += 1

dfs(1, numbers[0])
print(max_result)
print(min_result)