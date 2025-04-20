from itertools import permutations
import sys
sys.stdin = open("0413/chief_input.txt", "r")

def dfs(idx, selected, n, item):
    if len(selected) == n // 2:
        return calculate_taste(selected, item)

    if idx >= n:
        return float('inf')
    selected.append(idx)
    result1 = dfs(idx + 1, selected, n, item)
    selected.pop()
    result2 = dfs(idx + 1, selected, n, item)

    return min(result1, result2)


# def calculate_taste(group, item):
#     group2 = [i for i in range(len(item)) if i not in group]
#     taste1 = sum(item[i][j] + item[j][i] for i, j in permutations(group, 2))
#     taste2 = sum(item[i][j] + item[j][i] for i, j in permutations(group2, 2))
#     return abs(taste1 - taste2)


def calculate_taste(group, item):
    group2 = [i for i in range(len(item)) if i not in group]

    def sum_synergy(group):
        taste = 0
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                taste += item[group[i]][group[j]] + item[group[j]][group[i]]
        return taste

    taste1 = sum_synergy(group)
    taste2 = sum_synergy(group2)

    return abs(taste1 - taste2)

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    item = [list(map(int, input().split())) for _ in range(n)]

    min_diff = dfs(0, [], n, item)
    print(f"#{test_case} {min_diff}")
