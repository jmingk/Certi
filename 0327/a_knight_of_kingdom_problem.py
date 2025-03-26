# 8x8 정원
# 체스 나이트 움직임
# 모든 움직일 수 있는 경우의 수
#
N = "a1"
# 방법을 몰라서 유니코드 변환 방법 검색 ======
def convert(n):
    start_point = []
    col = ord(n[0]) - ord('a') + 1
    row = int(n[1])
    start_point.append(row)
    start_point.append(col)
    return start_point

start = convert(N)
count = 0
route = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for j in route:
    nr = start[0] + j[0]
    nc = start[1] + j[1]
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        count += 1

print(count)