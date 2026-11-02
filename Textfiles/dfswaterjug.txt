CAP_X = 4
CAP_Y = 3
INITIAL = (0, 0)
GOALS = {(2, 0), (0, 2)}
def get_successors(state):
    x, y = state
    successors = []
    if x < CAP_X:
        successors.append(((CAP_X, y), "Fill the 4-litre jug"))
    if y < CAP_Y:
        successors.append(((x, CAP_Y), "Fill the 3-litre jug"))
    if x > 0:
        successors.append(((0, y), "Empty the 4-litre jug"))
    if y > 0:
        successors.append(((x, 0), "Empty the 3-litre jug"))
    if x > 0 and y < CAP_Y:
        pour = min(x, CAP_Y - y)
        successors.append(((x - pour, y + pour), "Pour 4-litre jug into 3-litre jug"))
    if y > 0 and x < CAP_X:
        pour = min(y, CAP_X - x)
        successors.append(((x + pour, y - pour), "Pour 3-litre jug into 4-litre jug"))
    return successors
def dfs(initial, goals):
    stack = [initial]
    visited = {initial}
    parent = {initial: (None, "Start")}
    while stack:
        state = stack.pop()
        if state in goals:
            return reconstruct_path(parent, state)
        for next_state, action in reversed(get_successors(state)):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (state, action)
                stack.append(next_state)
    return None
def reconstruct_path(parent, state):
    path = []
    while state is not None:
        prev, action = parent[state]
        path.append((state, action))
        state = prev
    path.reverse()
    return path
def main():
    print("Water Jug Problem using DFS")
    print(f"Jugs: {CAP_X}L and {CAP_Y}L | Initial: {INITIAL} | Goal: (2, 0) or (0, 2)\n")
    path = dfs(INITIAL, GOALS)
    if path is None:
        print("No solution found.")
        return
    print("Solution path:")
    for step, (state, action) in enumerate(path):
        print(f"Step {step}: {state}  <- {action}")
    print(f"\nGoal reached in {len(path) - 1} steps.")
if __name__ == "__main__":
    main()