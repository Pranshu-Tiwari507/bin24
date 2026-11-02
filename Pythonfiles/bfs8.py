from collections import deque
INITIAL = (1, 2, 3,
           5, 6, 0,
           7, 8, 4)
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
MOVES = [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]
def is_solvable(state):
    tiles = [t for t in state if t != 0]
    inversions = sum(
        1 for i in range(len(tiles)) for j in range(i + 1, len(tiles))
        if tiles[i] > tiles[j]
    )
    return inversions % 2 == 0
def get_successors(state):
    successors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)
    for name, dr, dc in MOVES:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
            successors.append((tuple(new_state), name))
    return successors
def bfs(initial, goal):
    queue = deque([initial])
    visited = {initial}
    parent = {initial: (None, "Start")}
    while queue:
        state = queue.popleft()
        if state == goal:
            return reconstruct_path(parent, state)
        for next_state, move in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (state, move)
                queue.append(next_state)
    return None
def reconstruct_path(parent, state):
    path = []
    while state is not None:
        prev, move = parent[state]
        path.append((state, move))
        state = prev
    path.reverse()
    return path
def print_state(state):
    for r in range(0, 9, 3):
        print(" ".join("_" if t == 0 else str(t) for t in state[r:r + 3]))
def main():
    print("8-Puzzle using BFS\n")
    print("Initial state:")
    print_state(INITIAL)
    print("\nGoal state:")
    print_state(GOAL)
    print()
    if not is_solvable(INITIAL):
        print("This initial state is not solvable.")
        return
    path = bfs(INITIAL, GOAL)
    if path is None:
        print("No solution found.")
        return
    for step, (state, move) in enumerate(path):
        print(f"Step {step}: {move}" if step else "Step 0: Start")
        print_state(state)
        print()
    print(f"Goal reached in {len(path) - 1} moves.")
if __name__ == "__main__":
    main()