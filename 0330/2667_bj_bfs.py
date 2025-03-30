#bfs
import sys
sys.stdin = open("2667_input.txt", "r")

n = int(input())
for _ in range(n):
    arr = [0] + list(map(int, input().split()))
    visited =[0 for _ in range(n+1)]
    count = 0
    for i in range(1, n + 1):
        if (visited[i]) == 0:
            continue
        node = i
        count += 1
        visited[node] = 1
        node = arr[node]
        while :


    print(count)
