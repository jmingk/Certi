#input
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
def dfs_recursive(graph, start, visited = []):
    visited.append(start)
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    
    return visited

# main
visited = list()
dfs_recursive(graph, 'A', visited)
print(visited)