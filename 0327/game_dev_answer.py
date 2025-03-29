import sys

sys.stdin = open("dev_game_input.txt", "r")

n, m=map(int,input().split())
x,y,d=map(int, input().split())

#맵 정보 입력해 리스트에 저장
map_list=[]
for _ in range(n):
        row=list(map(int,input().split()))
        map_list.append(row)
map_list[x][y]=1

def rotation() :
    global d
    d-=1
    if d==-1 :
        d=3

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#시뮬레이션 시작
cnt=1
rotation_cnt=0
while True : 
    rotation()
    nx=x+dx[d]
    ny=y+dy[d]

    #회전한 이후 정면에 가보지 않은 칸이 있는 경우
    if map_list[nx][ny]==0 :
        map_list[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        rotation_cnt=0
        continue
    else :
        rotation_cnt+=1
    
    #네 방향 모두 갈 곳이 없을 경우
    if rotation_cnt==4 :
        nx=x-dx[d]
        ny=y-dy[d]
        if map_list[nx][ny]==0 :
            x=nx
            y=ny
        #뒤가 바다일 경우 탈출
        else :
            break
        rotation_cnt=0

print(cnt)