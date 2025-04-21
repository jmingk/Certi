# https://www.acmicpc.net/problem/10819
import sys
import heapq
sys.stdin = open("0423/input.txt", "rt")

def get_abs_result(series):
    global N
    total = 0
    for i in range(1, N):
        total += abs(series[i] - series[i-1])
    return total

max_total = 0
def comb(ns, visited = [], series = [], total = 0):
    global N, max_total
    if len(series) == N:
        # print(series)
        cur_total = get_abs_result(series)
        if cur_total > max_total:
            max_total = cur_total
        return
    for i in range(N):
        if visited[i]:
            continue
        series.append(ns[i])
        visited[i] = True
        comb(ns, visited, series)
        series.pop()
        visited[i] = False
    return

N = int(input())
ns = list(map(int, input().split(' ')))
visited = [False] * N
series = []
comb(ns, visited, series)
print(max_total)


