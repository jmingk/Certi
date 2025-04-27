n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

def dfs(index, result, plus, minus, mul, div):
    global max_value, min_value
    if index == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return

    if plus:
        dfs(index + 1, result + nums[index], plus - 1, minus, mul, div)
    if minus:
        dfs(index + 1, result - nums[index], plus, minus - 1, mul, div)
    if mul:
        dfs(index + 1, result * nums[index], plus, minus, mul - 1, div)
    if div:
        if result < 0:
            dfs(index + 1, -(-result // nums[index]), plus, minus, mul, div - 1)
        else:
            dfs(index + 1, result // nums[index], plus, minus, mul, div - 1)

dfs(1, nums[0], plus, minus, mul, div)

print(max_value)
print(min_value)
