# https://www.acmicpc.net/problem/2231

N = int(input())
result_list = []
for i in range(1, 1000000):
    str_n = str(i)
    string_list = list(str_n)
    int_list = list(map(int, string_list))

    first_num = i
    second_num = sum(int_list)
    sum_num = first_num + second_num

    if sum_num == N :
        result_list.append(first_num)
        break

if len(result_list) == 0:
    print(0)
else:
    print(min(result_list))

# def decom(n):
#     str_n = str(n)
#     string_list = list(str_n)
#     int_list = list(map(int, string_list))
#
#     first_num = n
#     second_num = sum(int_list)
#
#     sum_num = first_num + second_num
#
#     if sum_num != N and sum_num >= 1:
#         decom(n-1)
#         return
#     elif sum_num == N:
#         result_list.append(first_num)
#         decom(n-1)
#         return
#     else:
#         return
# decom(N)


