import sys
import heapq
sys.stdin = open("input.txt", "rt")

T = int(input())
for t in range(1,T+1):
    n,m,k,A,B = map(int, input().split()) # 접수창구 수, 정비창구 수, 고객 수
    A -= 1
    B -= 1
    접수창구 = list(map(int, input().split())) # 각 접수창구 처리시간
    정비창구 = list(map(int, input().split())) # 각 정비창구 처리시간
    도착시간 = list(map(int, input().split())) # 각 고객의 도착시간

    heapA = []
    for i in range(n):
        heapq.heappush(heapA, (0,i)) # 각 접수창구의 (끝나는 시간, 접수창구번호) 로 초기화
    heapB = []
    for i in range(m):
        heapq.heappush(heapB, (0,i)) # 각 정비창구의 (끝나는 시간, 정비창구번호)로 초기화

    # 각 고객 순서대로 진행
    temp = []
    users = [] # 접수창구를 이용한 고객들
    for i in range(k):
        time = 도착시간[i] # 현재 고객의 도착시간
        while heapA and heapA[0][0] <= time: # 끝나는시간이 도착시간보다 작으면 바로 진행 가능
            end_time, idx = heapq.heappop(heapA) # 해당 접수 (끝나는 시간,접수번호)
            heapq.heappush(temp, idx) # 어차피 접수 번호만 알면 돼

        if temp: # 이용 가능한 접수창구 존재 -> 번호 낮은 애들 순으로 저장 중.
            idx = heapq.heappop(temp)
            end_time = time + 접수창구[idx] # 현재 고객이 접수창구가 끝나는 시간
            heapq.heappush(users, (end_time, idx, i)) # (접수 창구 끝나는 시간, 접수창구번호, 현재 이용한 고객 인덱스)
            heapq.heappush(heapA, (end_time, idx))
        else: # 이용 가능한 접수창구 없으면..
            end_time, idx = heapq.heappop(heapA) # 가장 빨리 끝나는 접수창구
            end_time += 접수창구[idx] # 가장 먼저 끝나는 접수창구 시간 + 접수창구 시간
            heapq.heappush(users, (end_time, idx, i))
            heapq.heappush(heapA, (end_time, idx))
    # 정비창구 시작
    temp = []
    res = []
    while users: # 먼저 도착한 순서대로 꺼내서 진행 -> 도착 시간 같은 경우 접수창구 번호 우선
        end_timeA, idxA, userIdx = heapq.heappop(users)

        while heapB and heapB[0][0] <= end_timeA: # 정비창구 끝나는 시간이 더 빠르면 바로 가능
            _, idxB = heapq.heappop(heapB) # 정비창구 끝나는 시간, 정비창구 번호
            heapq.heappush(temp, idxB)

        if temp: # 이용 가능한 정비창구 존재
            idxB = heapq.heappop(temp)
            end_timeB = end_timeA + 정비창구[idxB]  # 정비창구 끝나는 시간
            heapq.heappush(heapB, (end_timeB, idxB))
            res.append((userIdx, idxA,idxB))
        else: # 이용 가능한 정비 창구가 없다면
            end_timeB, idxB = heapq.heappop(heapB) # 가장 먼저 끝나는 정비창구, 인덱스
            end_timeB += 정비창구[idxB]
            heapq.heappush(heapB, (end_timeB, idxB))
            res.append((userIdx, idxA,idxB))


    sum_idx = 0
    for userIdx, idxA,idxB in res:
        if idxA == A and idxB == B:
            sum_idx += (userIdx+1)

    if sum_idx == 0:
        print(f"#{t} {-1}")
    else:
        print(f"#{t} {sum_idx}")