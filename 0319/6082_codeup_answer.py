# https://codeup.kr/problem.php?id=6082

N = 33 #int(input())

for n in range(N):
    print(n, end=' ')
    print((str(n).find('3') != -1) or (str(n).find('6') != -1) or (str(n).find('9') != -1))


#

