"""
LAB 08: Graph Traversal - DFS and BFS

Required libraries:
- Python standard library only
- collections.deque is part of Python standard library

Theory:
DFS (Depth First Search):
Visits one branch as deeply as possible before backtracking.

BFS (Breadth First Search):
Visits vertices level by level using a queue.

Aim:
Implement DFS and BFS on the same graph.

Conclusion:
DFS uses recursion or a stack, while BFS uses a queue. Both are fundamental
graph traversal techniques.
"""

from collections import deque


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


def bfs(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


print("DFS traversal starting from A:")
dfs(graph, "A")

print("\n\nBFS traversal starting from A:")
bfs(graph, "A")
print()
