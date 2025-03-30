def fibo(n):
    # 메모이제이션을 위한 fibo_result
    fibo_result = {1:1, 2:1}
    # 3부터 N까지 피보나치 수열 값을 구함
    for i in range(3, n + 1):
        fibo_result[i] = fibo_result[i-1] + fibo_result[i-2]
    return fibo_result[n]

# fibonacci(N)을 구하라
N = 9
if N == 1 or N == 2:
    print(1)
else:
    result = fibo(N)
    print(result)