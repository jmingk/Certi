# https://codeup.kr/problem.php?id=6098

import sys
sys.stdin = open("input.txt", "r")

def Print(array) :
    for line in array :
        print(" ".join(map(str, line)))

array = []
for i in range(10):
    array.append(list(map(int, input().split())))

i = j = 1
while True :
    if array[i][j] == 2 : # On Food
        array[i][j] = 9
        Print(array)
        break
    else :
        array[i][j] = 9
    
    # go right
    if array[i][j + 1] == 0 or array[i][j + 1] == 2 :
        j += 1
    # go down
    elif array[i + 1][j] == 0 or array[i + 1][j] == 2 :
        i += 1
    # dont move
    else :
        Print(array)
        break
    