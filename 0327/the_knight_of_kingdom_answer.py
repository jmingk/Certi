xy = input()
x = ord(xy[0]) - ord('a')
y = xy[1] - 1

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

result = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx and nx <= 7 and 0 <= ny and ny <= 7 :
        result += 1

print(result)

