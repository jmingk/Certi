# https://www.acmicpc.net/problem/1182
import sys
import heapq
sys.stdin = open("0423/input.txt", "rt")

# ver 3: seq 제거
# 결과 : 34908 KB	228 ms

N, target = list(map(int, input().split(' ')))
ns = list(map(int, input().split(' ')))
cnt = 0

def dfs(i=0, cur_sum = 0):
    global N, target, ns, cnt

    if i >= N :
        if cur_sum == target:
            # print('#####target')
            cnt += 1
            return
        return
    
    dfs(i + 1, cur_sum)
    dfs(i + 1, cur_sum + ns[i])

if target == 0:
    cnt -= 1

dfs(0, 0)
print(cnt)