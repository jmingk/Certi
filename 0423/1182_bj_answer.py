# https://www.acmicpc.net/problem/1182
import sys
import heapq
sys.stdin = open("0423/input.txt", "rt")

# ver 2: cur_sum 캐싱 추가 
# 결과 : 34924 KB	380 ms
from collections import deque

N, target = list(map(int, input().split(' ')))
ns = list(map(int, input().split(' ')))
cnt = 0

def dfs(seq = [], i=0, cur_sum = 0):
    global N, target, ns, cnt
    # print(seq)

    if i >= N :
        if len(seq) > 0 and (cur_sum) == target:
            # print('#####target')
            cnt += 1
            return
        return
    
    dfs(seq, i + 1, cur_sum)
    dfs(seq + [ns[i]], i + 1, cur_sum + ns[i])

dfs([], 0, 0)
print(cnt)