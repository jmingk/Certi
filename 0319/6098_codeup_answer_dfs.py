import sys
sys.stdin = open("input.txt", "r")

N = [list(map(int, input().split())) for _ in range(10)]

arr = []
visit = [[0]*10]*10
for n in range(10):
    arr.append(N[n])

def maze(x, y):
    global N
    if N[x][y] == 2:
        N[x][y] = 9
        return
    else: 
        N[x][y] = 9
    
    if N[x][y + 1] != 1:
        maze(x, y + 1)
        return
    elif N[x + 1][y] != 1:
        maze(x + 1, y)
        return
    else:
        return


maze(1, 1)
for i in range(10):
    for j in range(10):
        print(N[i][j], end=" ")
    print()
