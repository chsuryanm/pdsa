from collections import deque, defaultdict

def bfs_shortest_path(graph, start):
    visited = {start: 0}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    
    return visited

# Example
graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
print(bfs_shortest_path(graph, 2))  # Output: {2: 0, 0: 1, 3: 1, 1: 2}
