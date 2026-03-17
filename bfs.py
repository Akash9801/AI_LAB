from collections import deque;

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
graph = {
    'A': ['D', 'C'],
    'D': ['B', 'E'],
    'C': ['F'],
    'B': [],
    'E': ['F'],
    'F': []
}
bfs(graph, 'A')