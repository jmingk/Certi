# https://www.acmicpc.net/problem/10819
from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
max_sum = 0

for perm in permutations(arr):
    total = 0
    for i in range(N - 1):
        diff = abs(perm[i] - perm[i + 1])
        total += diff
    max_sum = max(max_sum, total)

print(max_sum)
