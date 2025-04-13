# 입력 받고
N, K, 
pw

cnt = N // 4

arr = []
# 회전시키면서 숫자들 list에 담기
for i in range(cnt):
    # pw 밀기
    for j in range(pw.size()):
        # 밀기
    n = pw.pop()
    pw.insert(0, n)
    
    # pw = [1,B,3,B3B81F75E] -> 1B3 -> 10진수 (비교용)
    # 1B3 B3B .... 
    # cnt 갯수만큼 따로 분리하기 -> arr 담기
    for a in range(0, N, cnt):    # cnt = 3
        tmp = ''
        for b in range(a, a + cnt):
            tmp.append(b)   # -> 1B3
        arr.append(tmp)
    # arr  ['1B3', 'B3B', ...]

# 10진수 바꾸기
n_arr = []
for num in arr:
    n_arr.append(....)

# sorting






