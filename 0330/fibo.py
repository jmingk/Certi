# 바텀업
def fibo_b(n):
    DP_table = {1:1, 2:1}
    for i in range(3, n+1):
        DP_table[i] = DP_table[i-1] + DP_table[i-2]
    return DP_table[n]


N = 9
if N == 1 or N == 2:
    print(1)
else:
    result = fibo_b(N)
    print(result)



# 탑다운
def fibo(n):
    if n in DP_table:
        return DP_table[n]
    else:
        DP_table[n] = fibo(n-1) + fibo(n-2)
    return DP_table[n]

DP_table = {1:1, 2:1}
N = 10
result = fibo(10)

