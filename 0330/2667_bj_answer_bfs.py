# BFS
t = int(input())

for _ in range(t) :
  n = int(input())

  arr = [0] + list(map(int,input().split()))
  visited =[False for _ in range(n+1)]

  cycle = 0
  for i in range(1,n+1):    
    if (visited[i]) : continue
    cur_node = i
    cycle += 1
    visited[cur_node] = True
    cur_node = arr[cur_node]
    while True:
      if visited[cur_node] : break
      visited[cur_node] = True
      cur_node = arr[cur_node]
      
  print(cycle)