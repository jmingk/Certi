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
print(graph)

visited = []
def dfs(graph, start, visited):
    visited.append(start)
    for i in graph[start]:
        print(i)
        if i not in visited:
            dfs(graph, i, visited)
    return visited

dfs(graph, "A", visited)
print(visited)

