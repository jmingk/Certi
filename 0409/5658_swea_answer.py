T = int(input())

for t in range(T):
    N, K = map(int,input().split())
    pw = list(map(str,input()))
    cnt = N // 4 # 한 변당 번호 개수 = rotate수
    arr = [] # 회전 시킨 후 16진수 번호가 저장 될 리스트

    for i in range(cnt): # rotate 수 만큼 회전시킴
        pop = pw.pop() #리스트 끝 부분을 맨 앞으로 이동 시키면 한번 회전 완료됨
        pw.insert(0,pop)
        for j in range(0,N,cnt): # 리스트 내에서 각각 떨어져있는 요소를 하나의 번호로 합침 
            a = ''
            for k in range(j,j+cnt):
                a += pw[k]
            arr.append(a)

    new_arr = set(arr) # 중복을 허용치 않는 자료구조 set 활용
    answer = [] # 10진수로 변환된 숫자가 들어갈 리스트
    for num in new_arr: # 16진수 -> 10 진수로 변환
        answer.append(int(num,16))
        
    sorted_answer = sorted(answer,reverse=True) #내림차순 정렬
    print('#{} {}'.format(t+1,sorted_answer[K-1]))