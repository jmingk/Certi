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
        # cur_total = get_abs_result(series)
        if total > max_total:
            max_total = total
        return
    for i in range(N):
        if visited[i]:
            continue
        
        series.append(ns[i])
        visited[i] = True
        
        abs_result = 0
        if len(series) > 1:
            abs_result = abs(series[-1] - series[-2])
        
        total += abs_result

        comb(ns, visited, series, total)
        
        series.pop()
        visited[i] = False
        total -= abs_result
    return

N = int(input())
ns = list(map(int, input().split(' ')))
visited = [False] * N
series = []
comb(ns, visited, series, 0)
print(max_total)


