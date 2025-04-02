import sys
sys.stdin = open("up_stairs_input.txt", "r")

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))

dp = [0] * N
if N == 1:
    print(stairs[0])

dp[0] = stairs[0]
if N > 1 :
    dp[1] = stairs[0] + stairs[1]
else:
    dp[1] = stairs[1]

print(dp)
#
# for i in range(2, N):
#     dp[i] = max(dp[i-1] + stairs[i], dp[i-3] + stairs[i])
# print(dp[N-1])
