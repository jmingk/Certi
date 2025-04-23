# https://www.acmicpc.net/problem/1182
import sys
#sys.stdin = open("0423/input.txt", "rt")

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

def dfs(index, total):
    global count
    if index == N:
        return
    total += nums[index]
    if total == S:
        count += 1

    dfs(index + 1, total)
    dfs(index + 1, total - nums[index])

dfs(0, 0)
print(count)