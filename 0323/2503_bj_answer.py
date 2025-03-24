# 스트라이크, 볼 계산 함수
def get_score(guess, target):
    strike = sum(guess[i] == target[i] for i in range(3))
    ball = sum(g in target for g in guess) - strike
    return strike, ball

# 후보 숫자 생성 함수
def generate_candidates():
    result = []
    for i in range(1, 10):
        for j in range(1, 10):
            if j == i:
                continue
            for k in range(1, 10):
                if k == i or k == j:
                    continue
                result.append(f"{i}{j}{k}")
    return result

N = int(input())
questions = [input().split() for _ in range(N)]
questions = [(q, int(s), int(b)) for q, s, b in questions]

candidates = generate_candidates()

cnt = 0
for cand in candidates:
    valid = True
    for q, s, b in questions:
        cs, cb = get_score(q, cand)
        if cs != s or cb != b:
            valid = False
            break
    if valid:
        cnt += 1

print(cnt)