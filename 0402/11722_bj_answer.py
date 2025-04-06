import sys
sys.stdin = open("0402/input.txt", "r")

n = int(input())
nums = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if nums[j] > nums[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

