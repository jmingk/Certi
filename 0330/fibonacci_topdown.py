def fibo(n):
    # DP table에 있는 값이면 -> 이미 계산한 값 사용
    if n in DP_table:
        return DP_table[n]
    # DP table에 없는 값이면 -> 처음 계산
    else:
        DP_table[n] = fibo(n-1) + fibo(n-2)
    return DP_table[n]

# 메모이제이션을 위한 DP_table
DP_table = {1:1, 2:1}

# fibonacci(N)을 구하라
N = 10
result = fibo(N)
print(result)