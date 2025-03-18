#N = 55
N = int(input())
count = 0
result = 0

for i in range(N):
    if N > count:
        checker = i + 1
        count += checker
        result += 1
    else:
        print(result)
