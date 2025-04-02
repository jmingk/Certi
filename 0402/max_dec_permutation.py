N = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# dec_list = []
# count = 0
# min_num = min(arr)
# for i in range(N):
#     if arr[i] not in dec_list:
#         if count == 0 and min_num:
#             dec_list.append(arr[i])
#             count += 1
#         else:
#             max_index = len(dec_list) - 1
#             if arr[i] > dec_list[int(max_index)]:
#                 dec_list.append(arr[i])
#
# print(len(dec_list))