def transitive_closure(graph):
    reach = [[0] * len(graph) for _ in range(len(graph))]
    
    for i in range(len(graph)):
        for j in range(len(graph)):
            reach[i][j] = graph[i][j]
    
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    
    return reach

# Example
graph = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
print(transitive_closure(graph))  # Output: [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
