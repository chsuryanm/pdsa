from collections import defaultdict

def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    stack = [i for i in range(num_courses) if indegree[i] == 0]
    count = 0
    
    while stack:
        current = stack.pop()
        count += 1
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                stack.append(neighbor)
    
    return count == num_courses

# Examples
print(can_finish(2, [[1, 0]]))  # Output: True
print(can_finish(2, [[1, 0], [0, 1]]))  # Output: False
