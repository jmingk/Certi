# https://www.acmicpc.net/problem/1182
import sys
import heapq
sys.stdin = open("0423/input.txt", "rt")

# ver 1: dfs를 이용한 완전 탐색
# 결과 : 34908KB	488ms
from collections import deque

N, target = list(map(int, input().split(' ')))
ns = list(map(int, input().split(' ')))
cnt = 0

def dfs(seq = [], i=0):
    global N, target, ns, cnt

    if i >= N :
        if len(seq) > 0 and sum(seq) == target:
            # print(seq)
            # print('#####target')
            cnt += 1
            return
        return
    
    dfs(seq, i + 1)
    dfs(seq + [ns[i]], i + 1)

dfs([], 0)
print(cnt)