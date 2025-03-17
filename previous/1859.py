def test_code(value, max):
    global RES
    if max == int(0):
        max = value
    elif max != int(0):
        if value < max:
            RES += (max - value)
        elif value > max:
            max = value
    return max
         
 
T = int(input())
for test_case in range(T):
    N = int(input())
    global MAX
    MAX = 0
    RES = 0
    case = list(map(int, input().split()))
 
    for i in range(N, 0, -1):
        MAX = test_code(case[i-1], MAX)
 
    print(f"#{test_case + 1} {RES}")
