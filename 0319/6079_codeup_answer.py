# https://codeup.kr/problem.php?id=6079
#N = 55
N = int(input())
count = 0
result = 0

for i in range(1,N):
    if N > count:
        count += i
    else:
        print(i - 1)
        break

