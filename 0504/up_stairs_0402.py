# import heapq
#
# hq = heapq()
# N = int(input())
# stairs = []
# for _ in range(N):
#     stairs.append(int(input()))
#
# dp = [0] * N
# if N == 1:
#     print(stairs[0])
#
# dp[0] = stairs[0]
# if N > 1 :
#     dp[1] = stairs[0] + stairs[1]
# else:
#     dp[1] = stairs[1]
#
# print(dp)
#
# for i in range(2, N):
#     dp[i] = max(dp[i-1] + stairs[i], dp[i-3] + stairs[i])
# print(dp[N-1])
import sys
sys.stdin = open("up_stairs_input.txt", "r")

N = int(input())
stair = [0]*301
for i in range(N):
    stair[i]=int(input())

DP = [0]*301
DP[0] = stair[0]
DP[1] = stair[0]+stair[1]
DP[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, N):
    DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2]+stair[i])

print(DP[N-1])
