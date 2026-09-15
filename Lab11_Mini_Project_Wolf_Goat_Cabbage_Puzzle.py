"""
LAB 11 MINI PROJECT: Logical Puzzle Solver - Wolf, Goat, and Cabbage

Required libraries:
- Python standard library only
- collections.deque is part of the standard library

Problem:
A farmer must take a wolf, a goat, and a cabbage across a river.

Rules:
1. The boat can carry the farmer and at most one item.
2. The wolf cannot be left alone with the goat.
3. The goat cannot be left alone with the cabbage.

Theory:
The puzzle can be modeled as a state-space graph.
Each valid state is a graph node, and each legal boat movement is an edge.
BFS is used to find the shortest solution.

Conclusion:
Logical puzzles can be solved by representing valid situations as states and
using graph-search algorithms such as BFS.
"""

from collections import deque


# State format: (Farmer, Wolf, Goat, Cabbage)
# 0 = left bank
# 1 = right bank

start = (0, 0, 0, 0)
goal = (1, 1, 1, 1)
names = ["Farmer", "Wolf", "Goat", "Cabbage"]


def is_valid(state):
    farmer, wolf, goat, cabbage = state

    # Wolf eats goat if they are together without farmer
    if wolf == goat and farmer != wolf:
        return False

    # Goat eats cabbage if they are together without farmer
    if goat == cabbage and farmer != goat:
        return False

    return True


def possible_moves(state):
    farmer, wolf, goat, cabbage = state
    positions = list(state)

    # Farmer moves alone
    new_state = (1 - farmer, wolf, goat, cabbage)
    if is_valid(new_state):
        yield new_state, "Farmer crosses alone"

    # Farmer moves with one object on the same bank
    for i in range(1, 4):
        if positions[i] == farmer:
            new_positions = positions.copy()
            new_positions[0] = 1 - farmer
            new_positions[i] = 1 - positions[i]
            new_state = tuple(new_positions)

            if is_valid(new_state):
                yield new_state, f"Farmer takes {names[i]}"


def bfs_shortest_solution(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for next_state, move in possible_moves(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(
                    (next_state, path + [(move, next_state)])
                )

    return None


solution = bfs_shortest_solution(start, goal)

print("Wolf-Goat-Cabbage Puzzle")
print("0 = Left bank, 1 = Right bank")
print("Start:", start)

if solution is None:
    print("No solution found.")
else:
    print(f"\nShortest solution found in {len(solution)} moves:\n")
    current = start
    print("Step 0:", current)

    for step, (move, state) in enumerate(solution, start=1):
        print(f"Step {step}: {move}")
        print("        State:", state)
