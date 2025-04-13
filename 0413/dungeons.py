def dfs(k, dungeons, visited, count, max_dungeons):
    max_dungeons[0] = max(max_dungeons[0], count)

    for i in range(len(dungeons)):
        min_val, fatigue_cost = dungeons[i]
        if not visited[i] and k >= min_val:
            visited[i] = True
            dfs(k - fatigue_cost, dungeons, visited, count + 1, max_dungeons)
            visited[i] = False


def solution(k, dungeons):
    max_dungeons = [0]
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0, max_dungeons)
    return max_dungeons[0]