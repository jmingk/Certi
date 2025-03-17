global ten_x
ten_x = 0
# N = 29
N = int(input())
for i in range(N):
    checker = i + 1
    if checker < 10 and checker%3 == 0:
        print('X', end=" ")
    else:
        if checker%10 == 0:
            ten_x = checker
        if (checker-ten_x) != 0 and (checker-ten_x)%3 == 0:
            print("X", end=" ")
        else:
            print(checker, end=" ")
