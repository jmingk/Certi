import sys

sys.stdin = open("up_stairs_input.txt", "r")

N = int(input())
stairs = [int(input()) for _ in range(N)]

if N == 1:
    print(stairs[0])
    sys.exit()

dp = [0] * N
dp[0] = stairs[0]

if N > 1:
    dp[1] = stairs[0] + stairs[1]

for i in range(2, N):
    if i > 2:
        option1 = dp[i - 2] + stairs[i]
        option2 = dp[i - 3] + stairs[i - 1] + stairs[i]
        dp[i] = max(option1, option2)
    else:
        dp[i] = dp[i - 2] + stairs[i]

print(dp[N-1])