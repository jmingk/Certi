import sys
sys.stdin = open("input.txt", "r")

N = [list(map(int, input().split())) for _ in range(10)]

arr = []
visit = [[0]*10]*10
for n in range(10):
    arr.append(N[n])

def maze(x, y):
    visit[x][y] = 1
    arr[x][y] = 9
    if visit[x][y+1] == 0 and N[x][y+1] == 0:
        if maze(x, y+1):
            return True
    elif visit[x][y+1] == 0 and N[x][y+1] == 0 and N[x+1][y] == 0:
        if maze(x, y+1):
            return True
    elif visit[x][y+1] == 0 and N[x][y+1] != 0 and N[x+1][y] == 0:
        if maze(x+1, y):
            return True
    elif N[x][y+1] == 2:
        arr[x][y+1] = 9
    elif N[x+1][y] == 2:
        arr[x+1][y] = 9

    return False

maze(1, 1)
for i in range(10):
    for j in range(10):
        print(N[i][j], end=" ")
    print()
