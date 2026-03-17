

def dfs_tree(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop() 

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['P','R','T'],
    'F': ['S','O'],
    'P':[],
    'R':[],
    'T':[],
    'S':[],
    'O':[]
}

dfs_tree(graph, 'A')