from collections import deque

graph = {}
graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

visited = []

def bfs(graph, node, visited):
    que = deque(node)
    visited.append(node)
    while que:
        print(que)
        now_node = que.popleft()
        for next in graph[now_node]:
            if next not in visited:
                que.append(next)
                visited.append(next)

bfs(graph, "A", visited)
print(visited)