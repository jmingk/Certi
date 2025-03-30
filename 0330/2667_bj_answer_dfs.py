t = int(input().rstrip())

def dfs(graph, v, visited):
    while not visited[v]:
        visited[v] = True
        v = graph[v]  # 다음 노드로 이동
    return True

for _ in range(t):
    n = int(input().rstrip())
    g = list(map(int, input().strip().split()))


    # 그래프를 직접 1차원 리스트로 표현 (더 간결하고 빠름)
    graph = [0] + g  # 1-based index 사용
    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n + 1):
        if not visited[i]:  # 방문하지 않은 경우, 사이클 탐색 시작
            dfs(graph, i, visited)
            count += 1

    print(count)